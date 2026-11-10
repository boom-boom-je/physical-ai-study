# S0 · 환경 세팅 (11/2 ~ 11/8, 약 5시간)

## 새 PC에서 시작하기
학습은 NVIDIA GPU가 있는 데스크탑에서 한다.

1. 미리 설치: NVIDIA 드라이버, Git, Python 3.11(python.org 설치 파일. `py -3.11 --version`이 동작해야 한다), Claude Code
2. 짧은 영문 경로에 `jay-study` 브랜치로 받는다. 한글·괄호가 들어간 긴 경로는 일부 라이브러리나 Windows 경로 길이 제한에서 문제가 될 수 있다.
   ```powershell
   git clone -b jay-study https://github.com/boom-boom-je/physical-ai-study.git C:\dev\physical-ai-study
   ```
3. 비공개 파일(`CLAUDE.local.md`, `_private/`)은 git에 없으니 직접 복사해 온다.
4. 이 폴더에서 Claude Code를 열고 요청한다: "CLAUDE.md의 첫 세션 체크리스트대로 S0 진행해줘"

## 학습 목표
- [ ] `torch.cuda.is_available()`이 `True`로 나오는 환경을 직접 구성할 수 있다
- [ ] Gymnasium 환경을 만들고 `reset`·`step` 루프를 돌릴 수 있다
- [ ] HalfCheetah를 예로 관측·행동·보상이 각각 무엇인지 설명할 수 있다

## 설치 (Claude Code에 맡겨도 되는 부분)
1. `nvidia-smi`로 드라이버가 지원하는 CUDA 버전을 확인한다 (오른쪽 위 `CUDA Version`).
2. https://pytorch.org/get-started/locally/ 에서 Windows / Pip / Python / CUDA 버전(1번 값 이하)을 골라 `--index-url` 주소를 확인한다.
3. 저장소 루트에서 PowerShell로 실행한다.
   ```powershell
   powershell -ExecutionPolicy Bypass -File 00_setup\setup_windows.ps1 -TorchIndexUrl https://download.pytorch.org/whl/<cuda 태그>
   ```
   가상환경(`.venv`, Python 3.11) 생성 → CUDA PyTorch·torchvision → `requirements.txt` → 환경 확인 순서로 진행된다.
4. 확인을 통과하면 설치된 버전이 `00_setup/requirements-lock.txt`에 저장된다. 커밋해 둔다 (P1 재현용).
5. 확인만 다시 하려면: `.venv\Scripts\python.exe 00_setup\check_env.py`

> PyTorch를 `requirements.txt`보다 먼저 설치하는 이유: Stable-Baselines3가 PyTorch에 의존해서, 순서가 바뀌면 CPU 전용 PyTorch가 먼저 깔릴 수 있다.
>
> Python 3.11을 쓰는 이유: 3.14부터는 Box2D(S3의 LunarLander에 필요)가 Windows용 설치 파일이 없는 패키지로 바뀌어 빌드 도구가 필요하다.

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
- [ ] 설치 완료 (`check_env.py` 출력에서 CUDA True), `requirements-lock.txt` 커밋
- [ ] `random_agent.py`, `random_agent.gif`
- [ ] 위 질문에 대한 답 (이 파일 아래)
- [ ] `WEEKLY.md` 첫 기록

## 내 답

### 1. 관측 (observation)
- **17차원.** 칸 하나하나는 숫자 하나(스칼라)이고, 17개를 묶은 전체가 하나의 벡터다.
- **Num 0~7: 위치·각도.** 지금 몸이 어디에, 어떤 자세로 있는지 (단위 m, rad)

  | Num | 뜻 |
  |---|---|
  | 0 | 몸통 앞 끝의 높이 (z, m) |
  | 1 | 몸통의 기울기 각도 (rad) |
  | 2~4 | 뒷다리 허벅지·정강이·발 관절 각도 (rad) |
  | 5~7 | 앞다리 허벅지·정강이·발 관절 각도 (rad) |

- **Num 8~16: 속도·각속도.** 그 위치·각도가 얼마나 빠르게 변하고 있는지 (단위 m/s, rad/s)

  | Num | 뜻 |
  |---|---|
  | 8 | 몸통 앞 끝의 앞뒤(x) 속도 (m/s) |
  | 9 | 몸통 앞 끝의 위아래(z) 속도 (m/s) |
  | 10 | 몸통 기울기의 각속도 (rad/s) |
  | 11~13 | 뒷다리 허벅지·정강이·발 관절 각속도 (rad/s) |
  | 14~16 | 앞다리 허벅지·정강이·발 관절 각속도 (rad/s) |

- 정리하면 관절 6개 × (각도, 각속도) = 12개에 몸통 5개(높이, 기울기, 앞뒤 속도, 위아래 속도, 기울기 각속도)를 더해 17개다.
- 방향은 부호로 나타낸다. 예를 들어 8번이 +면 앞으로, -면 뒤로 움직이는 중이다.
- 위치·각도만으로는 사진 한 장처럼 "지금 어느 쪽으로 움직이는 중인지"를 알 수 없어서 속도도 함께 준다.
- **앞뒤 위치(x)가 빠진 이유:** 트랙의 어디에 있든 달리는 방법은 같아야 하기 때문이다. 자세를 제어하는 데는 높이·기울기·관절 각도와 그 속도만 있으면 되고, 앞뒤 위치는 필요 없다. 오히려 x를 넣으면 멀리 달려갈수록 학습 때 보지 못한 값이 들어와 정책이 헷갈릴 수 있다. 문서도 위치와 무관한 행동(position-agnostic behavior)을 유도하려고 뺀다고 설명한다. 앞으로 가는 **속도**(8번)는 보상과 바로 이어지므로 들어 있다.
- HalfCheetah는 앞뒤(x)와 위아래(z)로만 움직이는 2차원 모델이라 좌우 방향은 없다.

### 2. 행동 (action)
- **6차원, 각 값은 -1 ~ 1** (`Box(-1.0, 1.0, (6,), float32)`). 범위 안의 어떤 실수든 되는 **연속 행동**이다. CartPole은 0과 1 중 하나를 고르는 이산 행동이다.
- 각 값은 관절 6개에 각각 **얼마나 힘을 줄지 정하는 토크**(관절을 돌리는 힘, N·m)다. 부호는 회전 방향이다.

  | Num | 관절 |
  |---|---|
  | 0~2 | 뒷다리 허벅지·정강이·발 |
  | 3~5 | 앞다리 허벅지·정강이·발 |

- **관측과의 관계:** 토크는 회전을 빠르게 하거나 늦추는 힘이다(τ = Iα, F = ma의 회전 버전). 그래서 행동은 먼저 관절 각속도(관측 11~16)를 바꾸고, 그 변화가 쌓여 관절 각도(관측 2~7)가 바뀐다. 예: 행동 0(뒷다리 허벅지 토크) → 관측 11(각속도) → 관측 2(각도).
- 몸통(관측 0, 1, 8~10)에는 모터가 없다. 다리로 바닥을 밀어서 간접적으로만 움직일 수 있다.
