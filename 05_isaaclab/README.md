# S5 · Isaac Lab (2월, 약 20시간)

> Isaac Lab은 별도 설치·가상환경이 필요하다. 이 저장소의 `.venv`와 섞지 않는다. 설치 전에 공식 문서의 지원 OS·GPU 요구 사항을 확인한다.
>
> 데스크탑 GPU(RTX 3070 Ti, VRAM 8GB)는 최신 Isaac Sim 공식 최소 사양(RTX 4080, VRAM 16GB)보다 낮고, RAM 16GB도 최소 사양(32GB)보다 낮다. 2월 전에 화면 없이(headless) 실행하고 병렬 환경 수를 줄여 설치·학습이 되는지 먼저 시험한다. 안 되면 클라우드 GPU 같은 대안을 그때 정한다.

## 배울 것
GPU 병렬 시뮬레이션, Isaac Lab의 과제 구조, 도메인 랜덤화 설정, 지형 커리큘럼(쉬운 지형에서 어려운 지형으로 옮겨 가며 학습)

## 자료
- Isaac Lab 공식 문서 — 강화학습 예제 (RSL-RL로 ANYmal 속도 추종 과제 학습, 평지·거친 지형 버전): https://isaac-sim.github.io/IsaacLab/
- 논문: Rudin et al., 2021. Learning to Walk in Minutes Using Massively Parallel Deep RL (`papers/`에 요약)

## 학습 목표
- [ ] 수천 개 환경을 병렬로 돌려 보행 정책을 학습시킬 수 있다
- [ ] 과제 설정에서 도메인 랜덤화 항목(마찰, 질량 등)을 찾아 바꾸고 결과 차이를 확인할 수 있다
- [ ] 평지와 거친 지형 과제를 각각 학습해, 지형이 정책에 주는 영향을 설명할 수 있다
- [ ] MuJoCo 단일 환경 학습과 GPU 병렬 학습의 속도·결과 차이를 설명할 수 있다

## 산출물
- [ ] 학습된 보행 정책 영상 (평지 vs 거친 지형)
- [ ] 랜덤화 설정 변경 전후 비교 (`results/`)
- [ ] `/quiz` 1회 후 빠진 부분 보완

GPU 메모리가 부족하면 병렬 환경 수(`num_envs`)부터 줄인다.
