# S2 · 강화학습 기초 (11/16 ~ 12/6, 약 20시간)

> 튜터 모드: REINFORCE는 내가 직접 구현한다. Claude Code에는 개념 질문, 힌트, 리뷰만 요청한다.

## 배울 것
MDP, 보상·반환·할인율, 가치 함수, Q-learning, DQN, 정책 경사(REINFORCE)

## 자료
- Hugging Face Deep RL Course 유닛 1~4: https://huggingface.co/learn/deep-rl-course
- 한국어 번역 (위키독스): https://wikidocs.net/book/18941
- 보조: OpenAI Spinning Up "Key Concepts in RL": https://spinningup.openai.com

## 학습 목표
- [ ] MDP의 구성 요소(상태, 행동, 보상, 전이, 할인율)를 HalfCheetah에 대입해 설명할 수 있다
- [ ] 가치 기반(Q-learning)과 정책 기반(REINFORCE) 방법의 차이를 설명할 수 있다
- [ ] PyTorch로 REINFORCE를 직접 구현해 CartPole을 학습시킬 수 있다

## 산출물
- [ ] `reinforce_cartpole.py` — 직접 구현, 학습 곡선 그래프 (`results/`)
- [ ] `notes.md` — 유닛별 반 페이지 개념 정리 (유닛 1~4)

## 설명해 보기 (면담 대비)
1. 할인율 γ를 0.9와 0.99로 바꾸면 무엇이 달라지나?
2. REINFORCE의 분산이 큰 이유는? 베이스라인은 왜 도움이 되나?
3. on-policy와 off-policy의 차이는?

## 내 답
<!-- 여기에 적기 -->
