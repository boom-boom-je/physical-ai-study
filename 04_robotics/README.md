# S4 · 로봇공학 기초 (1월, 약 32시간)

## 배울 것
회전 행렬, 동차 변환, 순기구학, 자코비안 개념, 동역학 개요 (질량·관성·마찰이 운동에 미치는 영향), PD 제어(목표 각도와의 오차·속도로 토크를 계산하는 제어)와 토크 직접 제어의 차이

## 자료
- Modern Robotics (Lynch & Park) 2~5장, 8장 일부, 11장의 PD·PID 부분 — 무료 PDF·강의 영상: https://hades.mech.northwestern.edu/index.php/Modern_Robotics
- MuJoCo 모델 파일(MJCF) 문서: https://mujoco.readthedocs.io
- 수학: 회전·좌표 변환 (`math/` 1월)

## 학습 목표
- [ ] 회전 행렬과 동차 변환으로 좌표계 사이의 변환을 계산할 수 있다
- [ ] 2링크 로봇 팔의 순기구학을 코드로 구현할 수 있다
- [ ] MJCF에서 질량·관성·마찰·감쇠가 정의된 위치를 찾아 바꿀 수 있다
- [ ] PD 제어기가 목표 각도를 토크로 바꾸는 과정을 설명하고, HalfCheetah(토크 직접 제어)와 보행 로봇 RL(목표 각도 + PD 제어)의 차이를 말할 수 있다

## 산출물
- [ ] `two_link_fk.py` — 2링크 팔 순기구학, MuJoCo 시뮬레이션 결과와 비교
- [ ] `mjcf_physics_notes.md` — HalfCheetah MJCF의 물리 파라미터 정리 (Project 1·2에서 바꾸는 값과 연결)
- [ ] `/quiz` 1회 후 빠진 부분을 아래에 보완

## 내 답·메모
<!-- 여기에 적기 -->
