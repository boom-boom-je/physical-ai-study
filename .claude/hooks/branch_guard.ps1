# Claude Code PreToolUse hook for Bash/PowerShell: keeps all git work on the jay-study branch (CLAUDE.md).
# Exit 2 (blocked): creating/renaming/deleting branches, new worktrees, switching to any branch
# but jay-study, history-changing commands while HEAD is not jay-study, pushes to any other ref.
# ponytail: string-level parsing; git aliases, update-ref or scripts that call git slip through.
#           A GitHub branch rule that locks main is the upgrade path.
# Self-check: powershell -NoProfile -File .claude/hooks/branch_guard.ps1 -SelfTest
param([switch]$SelfTest)

$Allowed = 'jay-study'
$Strip = [char[]]'"''()'
$ReadOnlyBranchArgs = '-a', '--all', '-r', '--remotes', '-l', '--list', '-v', '-vv', '--verbose', '--show-current', '--no-color'
$HistoryCommands = 'commit', 'merge', 'rebase', 'reset', 'revert', 'cherry-pick', 'pull', 'push', 'am'

function Get-Block([string]$Cmd, [scriptblock]$Head) {
    foreach ($seg in ($Cmd -split '&&|\|\||[;|\r\n]')) {
        if (-not ($seg -match '(?:^|[\s(])git(?:\.exe)?\s+(.+)$')) { continue }
        $t = @(($Matches[1].Trim() -split '\s+') | ForEach-Object { $_.Trim($Strip) } | Where-Object { $_ })
        $i = 0
        while ($i -lt $t.Count -and $t[$i] -like '-*') { if ($t[$i] -in '-C', '-c') { $i++ }; $i++ }
        if ($i -ge $t.Count) { continue }
        $sub = $t[$i]
        $rest = @()
        foreach ($tok in ($t | Select-Object -Skip ($i + 1))) {
            if ($tok -match '^(\d*[<>]|&>)') { break }  # shell redirection: git's own arguments end here
            $rest += $tok
        }
        $pos = @($rest | Where-Object { $_ -notlike '-*' })

        if ($sub -in 'checkout', 'switch') {
            if ($rest | Where-Object { $_ -cmatch '^(-[bBcC].*|--orphan.*|--create.*|--force-create.*|--detach|-)$' }) {
                return "git $sub may not create a branch or leave $Allowed"
            }
            $fileRestore = $sub -eq 'checkout' -and $rest -contains '--'
            if (-not $fileRestore -and $pos.Count -gt 0 -and $pos[0] -ne $Allowed) {
                return "git $sub may only switch to $Allowed (got '$($pos[0])')"
            }
        }
        elseif ($sub -eq 'branch' -and ($rest | Where-Object { $_ -notin $ReadOnlyBranchArgs })) {
            return 'git branch may only list branches'
        }
        elseif ($sub -eq 'worktree' -and $pos -contains 'add') { return 'git worktree add is not allowed' }
        elseif ($sub -eq 'stash' -and $pos -contains 'branch') { return 'git stash branch is not allowed' }
        elseif ($sub -eq 'push') {
            if ($rest | Where-Object { $_ -in '--all', '--mirror', '--delete', '-d', '--prune' }) {
                return "git push may only update $Allowed"
            }
            foreach ($r in @($pos | Select-Object -Skip 1)) {
                $dst = ($r.TrimStart('+') -split ':')[-1]
                if ($r -like ':*' -or $dst -notin $Allowed, "refs/heads/$Allowed", 'HEAD') {
                    return "git push may only update $Allowed (got '$r')"
                }
            }
        }

        if ($sub -in $HistoryCommands) {
            $cur = "$(& $Head)".Trim()
            if ($cur -ne $Allowed) { return "HEAD is '$cur'; run 'git switch $Allowed' first" }
        }
    }
    return $null
}

if ($SelfTest) {
    $cases = @(
        # command, HEAD, expect blocked
        @('git status', 'main', $false),
        @('git switch jay-study', 'main', $false),
        @('git checkout -b feature', 'jay-study', $true),
        @('git switch -c x', 'jay-study', $true),
        @('git switch -', 'jay-study', $true),
        @('git checkout main', 'jay-study', $true),
        @('git checkout -- README.md', 'jay-study', $false),
        @('git branch -a', 'jay-study', $false),
        @('git branch new', 'jay-study', $true),
        @('git branch -D jay-study', 'jay-study', $true),
        @('git worktree add ../x', 'jay-study', $true),
        @('git commit -m "S1: x"', 'main', $true),
        @('cd repo && git commit -m "S1: x"', 'jay-study', $false),
        @('git -C . commit -m x', 'main', $true),
        @('git push origin main', 'jay-study', $true),
        @('git push origin jay-study:main', 'jay-study', $true),
        @('git push origin :jay-study', 'jay-study', $true),
        @('git push -u origin jay-study', 'jay-study', $false),
        @('git push', 'main', $true),
        @('echo $(git branch --show-current)', 'jay-study', $false),
        @('ls .git; cat README.md', 'main', $false),
        @('git push origin jay-study 2>&1', 'jay-study', $false),
        @('git push origin main 2>&1', 'jay-study', $true),
        @('git branch -a 2>$null', 'jay-study', $false),
        @('git status > out.txt', 'main', $false)
    )
    $fail = 0
    foreach ($c in $cases) {
        $h = $c[1]
        $got = [bool](Get-Block $c[0] { $h }.GetNewClosure())
        if ($got -ne $c[2]) { $fail++; Write-Host "FAIL: [$($c[0])] HEAD=$h blocked=$got" }
    }
    if ($fail) { exit 1 }
    Write-Host "OK: $($cases.Count) cases"
    exit 0
}

$ms = New-Object System.IO.MemoryStream
[Console]::OpenStandardInput().CopyTo($ms)
$json = [Text.Encoding]::UTF8.GetString($ms.ToArray()).TrimStart([char]0xFEFF)
$cmd = [string](ConvertFrom-Json $json).tool_input.command
if ($cmd -notmatch '\bgit\b') { exit 0 }
$dir = if ($env:CLAUDE_PROJECT_DIR) { $env:CLAUDE_PROJECT_DIR } else { '.' }
$reason = Get-Block $cmd { git -C $dir branch --show-current 2>$null }
if ($reason) {
    [Console]::Error.WriteLine("Blocked by .claude/hooks/branch_guard.ps1: $reason. All work stays on '$Allowed' (CLAUDE.md); do not create other branches.")
    exit 2
}
exit 0
