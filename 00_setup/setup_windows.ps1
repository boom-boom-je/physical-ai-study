# Sets up the Python environment for this repository on Windows.
#   1) creates .venv with Python 3.11 (py launcher, or "python" if that is 3.11)
#   2) installs the CUDA build of PyTorch + torchvision from the given index URL
#   3) installs requirements.txt
#   4) runs 00_setup\check_env.py
#   5) if the check passes, saves exact versions to 00_setup\requirements-lock.txt (commit it)
#
# Usage (PowerShell, from the repository root):
#   powershell -ExecutionPolicy Bypass -File 00_setup\setup_windows.ps1 -TorchIndexUrl https://download.pytorch.org/whl/<cuda-tag>
# Pick <cuda-tag> for your driver at https://pytorch.org/get-started/locally/

param(
    [string]$TorchIndexUrl = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

if ($TorchIndexUrl -eq "") {
    Write-Host "Missing -TorchIndexUrl."
    Write-Host "1) Run nvidia-smi to see the CUDA version your driver supports."
    Write-Host "2) Open https://pytorch.org/get-started/locally/ and copy the --index-url for Windows + Pip."
    Write-Host "3) Run: powershell -ExecutionPolicy Bypass -File 00_setup\setup_windows.ps1 -TorchIndexUrl <url>"
    exit 1
}

$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $venvPython)) {
    Write-Host "Creating virtual environment in .venv ..."
    $created = $false
    if (Get-Command py -ErrorAction SilentlyContinue) {
        & py -3.11 -m venv .venv
        if ($LASTEXITCODE -eq 0) { $created = $true }
        else { Write-Host "Python 3.11 not found via py launcher; trying 'python'." }
    }
    if (-not $created) {
        $ver = & python -c "import sys; print('%d.%d' % sys.version_info[:2])"
        if ($ver -ne "3.11") { throw "Python 3.11 is required (found '$ver'). Install it from python.org and retry." }
        & python -m venv .venv
        if ($LASTEXITCODE -ne 0) { throw "Could not create .venv." }
    }
}

Write-Host "Upgrading pip ..."
& $venvPython -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) { throw "pip upgrade failed." }

Write-Host "Installing PyTorch + torchvision (CUDA build) from $TorchIndexUrl ..."
& $venvPython -m pip install torch torchvision --index-url $TorchIndexUrl
if ($LASTEXITCODE -ne 0) { throw "PyTorch install failed. Check the index URL." }

Write-Host "Installing requirements.txt ..."
& $venvPython -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw "requirements install failed." }

Write-Host "Checking the environment ..."
& $venvPython 00_setup\check_env.py
if ($LASTEXITCODE -eq 0) {
    $lock = Join-Path $repoRoot "00_setup\requirements-lock.txt"
    [IO.File]::WriteAllLines($lock, [string[]](& $venvPython -m pip freeze))
    Write-Host "Saved exact package versions to 00_setup\requirements-lock.txt - commit it."
}
