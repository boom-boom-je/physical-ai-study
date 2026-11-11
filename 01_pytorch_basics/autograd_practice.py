import torch

# ① 다항식
x = torch.tensor(2.0, requires_grad=True)
y = (x ** 3) + (x * 2)
y.backward()
print(x.grad)

# ② 연쇄 법칙
x_1 = torch.tensor(2.0, requires_grad=True)
y_1 = (3 * x_1) + 1
z_1 = y_1 ** 2
z_1.backward()
print(x_1.grad)

# ③ 가중치 벡터
w = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
x_2 = torch.tensor([4.0, 5.0, 6.0], requires_grad=False)
y_2 = w * x_2
y_2_sum = y_2.sum()
print("y_2의 합:", y_2_sum)
y_2_sum.backward()
print(w.grad)
print(x_2.grad)

# ④ 기울기는 쌓일까?
y_3 = w * x_2
y_3_sum = y_3.sum()
print("y_3의 합:", y_3_sum)
y_3_sum.backward()
print(w.grad)
print(x_2.grad)
w.grad.zero_()
y_3 = w * x_2
y_3_sum = y_3.sum()
y_3_sum.backward()
print(w.grad)
print(x_2.grad)