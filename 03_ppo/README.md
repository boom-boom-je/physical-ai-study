# S3 · Actor-Critic과 PPO (12/7 ~ 12/31, 약 22시간)

> 튜터 모드: `ppo_from_scratch.py`는 내가 직접 쓴다. 면담에서 "PPO가 왜 이렇게 동작하나요?"에 답할 수 있어야 한다.

## 배울 것
Actor-Critic, 어드밴티지(Advantage), GAE, PPO의 클리핑 목적함수, 주요 하이퍼파라미터의 의미, 연속 행동 정책(가우시안 정책: 평균과 표준편차를 내서 행동을 뽑는 정책), 관측 정규화(관측값의 평균·분산을 맞춰 주는 처리)

## 자료
- Hugging Face Deep RL Course 유닛 6, 8 (유닛 8에서 CleanRL 구현을 기반으로 PPO를 직접 작성)
- CleanRL `ppo.py`(이산 행동), `ppo_continuous_action.py`(연속 행동): https://docs.cleanrl.dev
- 논문: Schulman et al., 2017. Proximal Policy Optimization Algorithms (`papers/`에 요약)

## 학습 목표
- [ ] PPO를 직접 구현해 LunarLander(이산 행동)를 학습시킬 수 있다
- [ ] 같은 코드를 연속 행동으로 확장해 HalfCheetah를 학습시킬 수 있다
- [ ] 클리핑이 왜 필요한지, 어드밴티지가 무엇인지 말로 설명할 수 있다
- [ ] HalfCheetah에서 직접 구현한 PPO와 SB3 PPO(P1-M1 기준 정책)의 학습 곡선을 비교하고 차이를 해석할 수 있다

## 산출물
- [ ] `ppo_from_scratch.py` — LunarLander(이산)에서 시작해 HalfCheetah(연속)로 확장
- [ ] SB3 PPO와의 학습 곡선 비교 그래프 (`results/`)
- [ ] `ppo_one_page.md` — PPO 한 페이지 설명 (면담용)
- [ ] `/quiz` 1회 후 빠진 부분을 "내 답"에 보완
- [ ] `KEYWORD.md`: S3 핵심 개념 정리 (면담·복습용)

일정이 밀리면 연속 행동 확장은 1월 초로 넘긴다 (Project 1 우선).

## 설명해 보기 (면담 대비)
1. 클리핑 범위 ε를 크게/작게 하면 학습이 어떻게 달라지나?
2. GAE의 λ는 무엇을 조절하나?
3. 같은 데이터로 여러 epoch 업데이트해도 되는 이유는?
4. 연속 행동에서 정책은 행동을 어떻게 뽑고, 그 행동의 로그 확률은 어떻게 계산하나?

## 내 답
<!-- 여기에 적기 -->
