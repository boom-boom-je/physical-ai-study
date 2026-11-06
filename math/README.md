# 수학 트랙 (매주 3시간 병행)

> 노트는 내가 쓴다. Claude Code에는 검토(`/review math/...`)와 연습 문제를 요청한다.
> 개념마다 "어느 코드나 논문에서 쓰였는지"를 한 줄씩 연결해 둔다.
> 순서는 그 달의 학습 단계에서 바로 쓰는 것부터 배치했다.

| 시기 | 주제 | 자료 | 학습 목표 | 노트 |
|---|---|---|---|---|
| 11월 | 선형대수(벡터, 행렬 곱, 선형변환, 역행렬, 고유값) + 미분 기초(편미분, 연쇄 법칙) | 3Blue1Brown "Essence of Linear Algebra", "Essence of Calculus"의 연쇄 법칙 편, MML 2장·5장 앞부분 | 신경망 한 층을 행렬 곱으로 쓸 수 있다. 역전파를 연쇄 법칙으로 설명할 수 있다 (S1) | `linear_algebra.md`, `calculus.md` |
| 11월 말~12월 | 확률: 확률변수, 기댓값, 정규분포, 조건부 확률, 최대가능도 | MML 6장 | 정책 경사와 PPO 목적함수의 기댓값·로그 확률 표기를 읽을 수 있다 (S2·S3) | `probability.md` |
| 1월 | 회전·좌표 변환(회전 행렬, 동차 변환) + 최적화(경사 하강법) | Modern Robotics 3장, MML 7장 | 회전 행렬이 선형변환임을 설명하고 좌표계 사이의 변환을 계산할 수 있다 (S4). 학습률이 경사 하강에 주는 영향을 설명할 수 있다 | `rotations.md`, `calculus.md` 보강 |

- MML: Mathematics for Machine Learning (Deisenroth 외), 무료 PDF: https://mml-book.github.io
- 3Blue1Brown: https://www.3blue1brown.com/topics/linear-algebra , https://www.3blue1brown.com/topics/calculus

## 노트 형식
```
## 개념 이름
- 한 줄 정의:
- 직관 (그림이나 예):
- 어디에 쓰이나 (코드/논문):
- 헷갈렸던 점:
```
