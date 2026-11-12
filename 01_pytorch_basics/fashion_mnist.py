import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import v2
import matplotlib.pyplot as plt


training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])
)

# ① 창고 두 개
print("학습용 데이터 셋의 크기:", len(training_data))
print("테스트용 데이터 셋의 크기:", len(test_data))

# ② 한 개 꺼내 보기
picture, answer = training_data[0]
print("사진의 타입:", type(picture))
print("사진의 모양:", picture.shape)
print("사진의 자료형:", picture.dtype)
print("사진의 최소/최대:", picture.min(), picture.max())
print(training_data.classes[answer])

# ③ 컨베이어 두 개
from torch.utils.data import DataLoader

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=False)

X, y = next(iter(train_dataloader))
print("사진 묶음, 정답 묶음의 크기:", len(train_dataloader))
print("사진 묶음, 정답 묶음의 모양:", X.shape, y.shape)

# ④ 묶음 세기
for pictures, answers in train_dataloader:
    last_pictures_count = pictures.shape[0]
print("마지막 묶음 장 수:", last_pictures_count)


# ① 모델 정의
from torch import nn
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork()

# ② GPU로
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
print(model)

# ③ 통과시키기
X = X.to(device)
logits = model(X)
print("모델 X의 출력 모양:", logits.shape)

# ④ 에측과 정답 비교
y = y.to(device)
pred = logits.argmax(dim=1)
print("모델 X의 예측:", pred[:10])
print("모델 X의 정답:", y[:10])

acc = (pred == y).float().mean().item()
print("학습 전 정확도(%):", acc * 100)

# ⑤ 가중치 개수
total = 0
for p in model.parameters():
    total += p.numel()
print("가중치 개수:", total)


# ① 학습 전 손실
