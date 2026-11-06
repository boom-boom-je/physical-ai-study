# 논문 읽기 트랙 (매주 약 2시간, 컨택 준비 포함)

> 요약은 내가 쓴다. Claude Code에는 내 요약의 검토와 "이해했는지 확인하는 질문"(`/quiz`)을 요청한다.

## 읽는 순서
| 시기 | 논문 | 왜 읽는가 | 연결 |
|---|---|---|---|
| 상시 | 컨택할 연구실의 최근 논문 (곳당 1편, 메일 보내기 전에) | 컨택 메일·면담 준비 | 컨택 |
| 12월 초 | Peng et al., 2018. Sim-to-Real Transfer of Robotic Control with Dynamics Randomization (ICRA) — arxiv.org/abs/1710.06537 | 물리 값 랜덤화의 대표 논문 | P1-M3 |
| 12월 말 | Schulman et al., 2017. Proximal Policy Optimization Algorithms — arxiv.org/abs/1707.06347 | 직접 구현한 알고리즘의 원문 | S3 |
| 1월 초 | Hwangbo et al., 2019. Learning Agile and Dynamic Motor Skills for Legged Robots (Science Robotics) — arxiv.org/abs/1901.08652 | 보행 로봇 sim-to-real, 액추에이터 네트워크 | P2, S4 PD 제어 |
| 1월 중 | Yu et al., 2017. Preparing for the Unknown: Learning a Universal Policy with Online System Identification (RSS) — arxiv.org/abs/1702.02453 | 물리 값을 직접 추정해 정책에 넣는 방법(UP-OSI). P2와 구조가 거의 같다 | P2 |
| 1월 중 | Kumar et al., 2021. RMA: Rapid Motor Adaptation for Legged Robots (RSS) — arxiv.org/abs/2107.04034 | 현실 적응의 대표 방법. UP-OSI와 비교하며 읽는다 | P2 |
| 1월 말 | Nagabandi et al., 2019. Learning to Adapt in Dynamic, Real-World Environments Through Meta-Reinforcement Learning (ICLR) — arxiv.org/abs/1803.11347 | 학습한 동역학 모델(세계 모델)을 최근 데이터로 빠르게 고쳐 적응한다. HalfCheetah 실험 포함 | 연구 방향, P2-M5 |
| 2월 | Rudin et al., 2021. Learning to Walk in Minutes Using Massively Parallel Deep RL (CoRL) — arxiv.org/abs/2109.11978 | GPU 병렬 학습, 지형 커리큘럼 | S5 |
| 2월 | Wu et al., 2022. DayDreamer: World Models for Physical Robot Learning (CoRL) — arxiv.org/abs/2206.14176 | 세계 모델로 실제 로봇을 직접 학습 | 연구 방향, P2 보고서 "다음 단계" |

## 읽는 방법
1회차: 초록·그림·결론만 (30분) → 2회차: 방법 (수식은 표기만 확인) → 3회차: 내 프로젝트 관점에서 정리. 번역 도구를 써도 된다.

## 목표
논문 한 편의 문제, 핵심 아이디어, 실험, 한계를 5분 안에 말로 설명할 수 있다.

## 산출물
논문당 한 파일: `YYYY_저자_키워드.md` (예: `2021_kumar_rma.md`). 형식은 `_template.md`.
