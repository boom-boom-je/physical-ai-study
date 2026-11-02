# S5 · Isaac Lab (2월, 약 20시간)

> Isaac Lab은 별도 설치·가상환경이 필요하다. 이 저장소의 `.venv`와 섞지 않는다. 설치 전에 공식 문서의 지원 OS·GPU 요구 사항을 확인한다.

## 배울 것
GPU 병렬 시뮬레이션, Isaac Lab의 과제 구조, 도메인 랜덤화 설정

## 자료
- Isaac Lab 공식 문서 — 강화학습 예제 (RSL-RL로 ANYmal 속도 추종 과제 학습): https://isaac-sim.github.io/IsaacLab/
- 논문: Rudin et al., 2021. Learning to Walk in Minutes Using Massively Parallel Deep RL (`papers/`에 요약)

## 학습 목표
- [ ] 수천 개 환경을 병렬로 돌려 보행 정책을 학습시킬 수 있다
- [ ] 과제 설정에서 도메인 랜덤화 항목(마찰, 질량 등)을 찾아 바꾸고 결과 차이를 확인할 수 있다
- [ ] MuJoCo 단일 환경 학습과 GPU 병렬 학습의 속도·결과 차이를 설명할 수 있다

## 산출물
- [ ] 학습된 보행 정책 영상
- [ ] 랜덤화 설정 변경 전후 비교 (`results/`)

GPU 메모리가 부족하면 병렬 환경 수(`num_envs`)부터 줄인다.
