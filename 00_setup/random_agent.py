# gymnasium 호출
import gymnasium as gym

# 환경 생성
# "HalfCheetah-v5": 어떤 환경을 만들지
# render_mode; 어떻게 보여줄지
env = gym.make("HalfCheetah-v5", render_mode="rgb_array")

# 환경 리셋
observation, info = env.reset()

# 관측 출력
print(f"Starting observation: {observation}")

# 반복문 변수 설정
episode_over = False
total_reward = 0

# 에피소드 끝날 때 까지 한 스텝씩 반복
# 에피소드: reset부터 끝날 때 까지의 스텝의 묶음
# 스텝: 행동 1회
while not episode_over:
    # 이 환경에서 허용되는 행동의 범위
    # print(env.action_space) => Box(-1.0, 1.0, (6,), float32)
    # sample은 그 안에서 무작위로 하나의 벡터 뽑아서 실행
    action = env.action_space.sample()

    # 시뮬레이터가 행동을 한 스텝 씩 진행하고 값 돌려줌
    # terminated: 에피소드가 목표 달성에 성공 혹은 실패하면 종료
    # truncated: 에피소드 타임스텝이 종료되면 강제 종료
    observation, reward, terminated, truncated, info = env.step(action)

    # 보상 합계 출력, 에피소드 종료 출력
    total_reward += reward
    episode_over = terminated or truncated

# 종료
print(f"Episode finished! Total reward: {total_reward}")
env.close()