# S0 · 환경 세팅 (11/2 ~ 11/8, 약 5시간)

## 학습 목표
- [ ] `torch.cuda.is_available()`이 `True`로 나오는 환경을 직접 구성할 수 있다
- [ ] Gymnasium 환경을 만들고 `reset`·`step` 루프를 돌릴 수 있다
- [ ] HalfCheetah를 예로 관측·행동·보상이 각각 무엇인지 설명할 수 있다

## 설치 (Claude Code에 맡겨도 되는 부분)
1. `nvidia-smi`로 드라이버가 지원하는 CUDA 버전을 확인한다.
2. https://pytorch.org/get-started/locally/ 에서 Windows / Pip / Python / 내 CUDA 버전을 골라 `--index-url` 주소를 확인한다.
3. 저장소 루트에서 PowerShell로 실행한다.
   ```powershell
   powershell -ExecutionPolicy Bypass -File 00_setup\setup_windows.ps1 -TorchIndexUrl https://download.pytorch.org/whl/<cuda 태그>
   ```
   가상환경(`.venv`) 생성 → CUDA PyTorch → `requirements.txt` → 환경 확인 순서로 진행된다.
4. 확인만 다시 하려면: `.venv\Scripts\python.exe 00_setup\check_env.py`

> PyTorch를 `requirements.txt`보다 먼저 설치하는 이유: Stable-Baselines3가 PyTorch에 의존해서, 순서가 바뀌면 CPU 전용 PyTorch가 먼저 깔릴 수 있다.

## 과제 (직접 작성)
`00_setup/random_agent.py`를 직접 작성한다. 막히면 Claude Code에 **힌트**를 요청한다.

1. `HalfCheetah-v5` 환경을 `render_mode="rgb_array"`로 만든다.
2. 무작위 행동으로 300스텝 정도 실행하면서 매 스텝 화면(프레임)을 모은다.
3. 모은 프레임을 `imageio`로 GIF로 저장한다 → `00_setup/random_agent.gif`
4. 에피소드 보상 합계를 출력한다.

스스로 답해 볼 질문 (답은 이 파일 아래에 적어 둔다):
- 관측(observation)은 몇 차원이고 각각 무엇을 뜻하나?
- 행동(action)은 몇 차원이고 범위는?
- 보상은 어떤 항들로 이루어져 있나? 랜덤 에이전트의 보상은 왜 그 값이 나오나?
- `env.unwrapped.model.body_mass`에는 무엇이 들어 있나? (Project 1에서 바꿀 값)

참고: https://gymnasium.farama.org/environments/mujoco/half_cheetah/

## 산출물
- [ ] 설치 완료 (`check_env.py` 출력에서 CUDA True)
- [ ] `random_agent.py`, `random_agent.gif`
- [ ] 위 질문에 대한 답 (이 파일 아래)
- [ ] `WEEKLY.md` 첫 기록

## 내 답
<!-- 여기에 적기 -->
