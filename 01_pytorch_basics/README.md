# S1 · PyTorch 기초 (11/2 ~ 11/15, 약 12시간)

> 튜터 모드: 이 폴더의 코드는 내가 직접 쓴다. Claude Code에는 힌트와 리뷰(`/review`)만 요청한다.

## 배울 것
텐서, autograd, `nn.Module`, `Dataset`·`DataLoader`, 학습 루프, GPU 사용, 모델 저장·불러오기

## 자료
- PyTorch 공식 튜토리얼 "Learn the Basics" (FashionMNIST 예제): https://pytorch.org/tutorials/beginner/basics/intro.html
- 수학: 연쇄 법칙 (`math/` 11월). 아래 "설명해 보기" 1번에 필요하다

## 학습 목표
- [ ] 라이브러리 도움 없이 학습 루프(순전파 → 손실 → 역전파 → 업데이트)를 직접 작성할 수 있다
- [ ] autograd가 기울기를 계산하는 방식을 간단한 예로 설명할 수 있다
- [ ] 학습 곡선을 그리고 과적합 여부를 판단할 수 있다

## 산출물
- [ ] `fashion_mnist.py` (또는 노트북) — 직접 짠 학습 루프, 학습·검증 곡선 그래프
- [ ] `mlp_regression.py` — 간단한 MLP 회귀 (예: 노이즈 섞인 사인 곡선 맞추기). Project 2의 물리 값 추정기 예행연습
- [ ] 아래 "설명해 보기"에 대한 내 답
- [ ] `/quiz` 1회 후 빠진 부분을 "내 답"에 보완
- [ ] `KEYWORD.md`: S1 핵심 개념 정리 (면담·복습용)

## 설명해 보기 (면담 대비)
1. `loss.backward()`를 부르면 무슨 일이 일어나나?
2. `optimizer.zero_grad()`를 빼먹으면 어떻게 되나?
3. 학습 곡선에서 과적합은 어떻게 보이나?

## 내 답
<!-- 여기에 적기 -->
