import numpy as np
import torch

# ① 관측 묶음
# torch.rand로 (4, 17) 텐서를 만들어 obs에 저장하고 확인 4가지를 출력하세요.
obs = torch.rand(4, 17)
print("obs의 타입:", type(obs))
print("obs의 모양:", obs.shape)
print("obs의 자료형:", obs.dtype)
print("obs의 장소:", obs.device)

# ② 가장 단순한 "정책"
w = torch.rand(17, 6)
print("obs, w 행렬곱의 모양:", (obs @ w).shape)

# ③ GPU로
device = "cuda" if torch.cuda.is_available() else "cpu"
obs_g = obs.to(device)
w_g = w.to(device)
print("obs_g의 장소:", obs_g.device)
print("w_g의 장소:", w_g.device)
print("obs_g, w_g 행렬곱의 모양:", (obs_g @ w_g).shape)
print("obs_g, w_g 행렬곱의 장소:", (obs_g @ w_g).device)

# ④ S0 관측을 텐서로
import gymnasium as gym
env = gym.make("HalfCheetah-v5")
observation, info = env.reset(seed=0)
cheetah = torch.from_numpy(observation)
print("cheetah의 자료형(64):", cheetah.dtype)
# PyTorch 신경망의 가중치는 기본이 float32
# float64 관측을 그대로 넣으면 자료형이 달라 에러 발생
print("cheetah의 자료형(32):", cheetah.float().dtype)
print("cheetah의 모양:", cheetah.shape)
env.close()

# ⑤ 사진 펴기(수업 4 준비)
picture = torch.rand(8, 1, 28, 28)
picture_reshape = picture.reshape(8, -1)
print("picture의 모양:", picture_reshape.shape)