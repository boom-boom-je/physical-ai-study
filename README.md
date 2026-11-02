# physical-ai-study

시뮬레이션에서 학습한 로봇이 현실의 물리 변화(마찰, 질량, 지형)에 적응하는 문제를 공부하는 저장소입니다.
PyTorch와 강화학습 기초부터 시작해, MuJoCo에서 물리 값 변화에 대한 정책의 견고성을 측정하고(Project 1), 간단한 적응 모듈을 만드는 것(Project 2)까지 진행합니다.

## 진행 현황

| 단계 | 내용 | 기간 | 상태 |
|---|---|---|---|
| S0 | 환경 세팅 | 11/2~11/8 | ⬜ |
| S1 | PyTorch 기초 | ~11/15 | ⬜ |
| S2 | 강화학습 기초 (REINFORCE) | 11/16~12/6 | ⬜ |
| S3 | Actor-Critic, PPO 직접 구현 | 12/7~12/31 | ⬜ |
| P1-M1 | 기준 정책 (HalfCheetah + PPO) | 11/16~11/29 | ⬜ |
| P1-M2 | 물리 값 변화 견고성 평가 | 11/30~12/13 | ⬜ |
| P1-M3 | 도메인 랜덤화 비교 | 12/14~12/27 | ⬜ |
| P1-M4 | 정리·공개 | 12/28~12/31 | ⬜ |
| S4 | 로봇공학 기초 | 1월 | ⬜ |
| P2 | 적응 모듈 (RMA 단순화) | 1~2월 | ⬜ |
| S5 | Isaac Lab | 2월 | ⬜ |

상태: ⬜ 시작 전 · 🟨 진행 중 · ✅ 완료

## 구조

```
physical-ai-study/
├── CLAUDE.md              Claude Code 작업 규칙 (튜터 모드)
├── WEEKLY.md              주간 기록
├── requirements.txt
├── 00_setup/              S0 환경 세팅
├── 01_pytorch_basics/     S1
├── 02_rl_basics/          S2
├── 03_ppo/                S3
├── 04_robotics/           S4
├── 05_isaaclab/           S5
├── math/                  수학 노트
├── papers/                논문 요약
├── projects/
│   ├── p1_physics_robustness/
│   └── p2_adaptation/
└── docs/learning_guide.md 전체 학습 계획
```

## 시작하기

1. Claude Code에서 이 폴더를 연다 (아래 둘 중 하나).
   - Claude 데스크탑 앱: 설정 → Claude Code → "Use this computer from your phone and claude.ai"를 켜고 이 폴더를 추가한 뒤, 프로젝트 대화에서 **+ → Work locally**로 요청
   - 터미널: 이 폴더에서 `claude` 실행
2. 첫 요청: "CLAUDE.md의 첫 세션 체크리스트대로 S0 진행해줘"
3. 환경 세팅이 끝나면 `00_setup/README.md`의 과제(랜덤 에이전트 GIF)를 직접 작성한다.
