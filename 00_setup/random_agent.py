# gymnasium 호출
import gymnasium as gym
import imageio

# 환경 생성
# "HalfCheetah-v5": 어떤 환경을 만들지
# render_mode; 어떻게 보여줄지
# camera_name: 카메라 설정
# width, height: 화면 크기
env = gym.make("HalfCheetah-v5", render_mode="rgb_array", camera_name="track", width=320, height=320)

# 환경 리셋
observation, info = env.reset(seed=0)
env.action_space.seed(0)
frame = env.render()
print("type:", type(frame))
print("shape:", frame.shape)
print("dtype:", frame.dtype)
print("min/max:", frame.min(), frame.max())

# 관측 출력
print(f"Starting observation: {observation}")

# 반복문 변수 설정
# episode_over는 이제 쓰이지 않음: 300회 반복이기 때문에 truncated = True가 되지 않음
# HalfCheetah-v5에서 terminated는 항상 False -> 끝났는지 검사할 필요 X
total_reward = 0
frames = []

# 참고: Gymnasium "Basic Usage" 예제를 HalfCheetah에 맞게 고침
# 1 에피소드(1000 스텝) 중 300 스텝만 반복
# 에피소드: reset부터 끝날 때 까지의 스텝의 묶음
# 스텝: 행동 1회
for i in range(300):
    # 이 환경에서 허용되는 행동의 범위
    # print(env.action_space) => Box(-1.0, 1.0, (6,), float32)
    # sample은 그 안에서 무작위로 하나의 벡터 뽑는다
    action = env.action_space.sample()
    # terminated: 에피소드가 목표 달성에 성공 혹은 실패하면 종료
    # truncated: 에피소드 1000 스텝의 시간 제한이 종료되면 강제 종료
    observation, reward, terminated, truncated, info = env.step(action)
    # 보상 누적
    total_reward += reward
    # 매 스텝 움직일 때마다 찍고 리스트에 넣기
    frame = env.render()
    frames.append(frame)

print("shape:", frames[-1].shape)
# duration: 사진 한 장이 표시될 시간(ms 단위, 50=0.05초)
imageio.mimsave("00_setup/random_agent.gif", frames, duration=50, loop=0)

# 종료
print("반복횟수:", i+1)
print(f"300 Step done! Total reward: {total_reward}")
env.close()