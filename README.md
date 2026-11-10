# physical-ai-study

피지컬 AI 대학원 진학을 준비하며, 시뮬레이션에서 학습한 로봇이 현실의 물리 변화(마찰·질량·지형)에 적응하는 문제를 공부하는 저장소입니다.
PyTorch와 강화학습 알고리즘을 직접 구현하며 기초를 쌓고, MuJoCo에서 물리 값 변화에 대한 정책의 견고성을 측정한 뒤(Project 1) 간단한 적응 모듈을 만듭니다(Project 2).

## 연구 관심
가상 환경에서 학습한 로봇이 현실에 투입된 뒤, 마찰·질량·지형 같은 물리적 특성을 스스로 추정하고 내부의 세계 모델을 빠르게 고쳐 가며 적응하는 문제에 관심이 있습니다.

키워드: Sim-to-Real · Online Adaptation · System Identification · Model-based RL / World Model · Domain Randomization

## 최신 결과
<!-- 산출물이 나올 때마다 가장 최근 것 하나로 바꾼다: 그림(GIF·그래프) 한 장 + 한 줄 설명 + 해당 폴더 링크 -->
![HalfCheetah 랜덤 에이전트](00_setup/random_agent.gif)

**S0 · HalfCheetah-v5 랜덤 에이전트:** 무작위 토크로 300스텝(15초)을 움직인 결과입니다. 보상은 -103.8(시드 0)로, 앞으로 학습할 정책과 비교할 기준선입니다. → [`00_setup/`](00_setup/)

## 진행 현황
진행 기록은 `jay-study` 브랜치에 쌓이고, `main`은 학습 시작 전 초기 상태입니다.

| 단계 | 내용 | 기간 | 상태 |
|---|---|---|---|
| S0 | 환경 세팅 | 11/2~11/8 | ✅ |
| S1 | PyTorch 기초 | ~11/15 | 🟨 |
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

## 원칙
- 학습 단계의 코드, 연구 질문, 실험 설계, 결과 해석은 직접 합니다. Claude Code는 튜터(개념 질문·힌트·코드 리뷰)와 실험 보조(반복 실행 스크립트·설정 파일·그래프)에만 씁니다. 규칙은 [`CLAUDE.md`](CLAUDE.md)에 있습니다.
- 실험은 설정 파일, 시드 3개, 평균±표준편차로 기록합니다.
- 매주 [`WEEKLY.md`](WEEKLY.md)에 한 것 / 막힌 것 / 다음 주 할 것을 남깁니다.

## 구조

```
physical-ai-study/
├── CLAUDE.md              Claude Code 작업 규칙 (튜터 모드)
├── WEEKLY.md              주간 기록
├── requirements.txt
├── .claude/               Claude Code 명령(/progress 등), 브랜치 가드
├── 00_setup/              S0 환경 세팅 (새 PC에서 시작하는 방법)
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
