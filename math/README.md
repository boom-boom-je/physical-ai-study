# 수학 트랙 (매주 3~4시간 병행)

> 노트는 내가 쓴다. Claude Code에는 검토(`/review math/...`)와 연습 문제를 요청한다.
> 개념마다 "어느 코드나 논문에서 쓰였는지"를 한 줄씩 연결해 둔다.

| 시기 | 주제 | 자료 | 학습 목표 | 노트 |
|---|---|---|---|---|
| 11월 | 선형대수: 벡터, 행렬 곱, 선형변환, 역행렬, 고유값 | 3Blue1Brown "Essence of Linear Algebra", MML 2장 | 신경망 한 층을 행렬 곱으로 쓸 수 있다. 회전 행렬이 선형변환임을 설명할 수 있다 | `linear_algebra.md` |
| 12월 | 확률: 확률변수, 기댓값, 정규분포, 조건부 확률, 최대가능도 | MML 6장 | PPO 목적함수의 기댓값·로그 확률 표기를 읽을 수 있다 | `probability.md` |
| 1월 | 미분·최적화: 편미분, 연쇄 법칙, 경사 하강법 | MML 5장, 7장 | 역전파를 연쇄 법칙으로 설명할 수 있다 | `calculus.md` |

- MML: Mathematics for Machine Learning (Deisenroth 외), 무료 PDF: https://mml-book.github.io
- 3Blue1Brown: https://www.3blue1brown.com/topics/linear-algebra

## 노트 형식
```
## 개념 이름
- 한 줄 정의:
- 직관 (그림이나 예):
- 어디에 쓰이나 (코드/논문):
- 헷갈렸던 점:
```
