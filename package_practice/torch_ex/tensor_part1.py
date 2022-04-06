import torch

a = torch.arange(4*4).view(4,4)

print("tensor 4 X 4:\n", a)
print("tensor sum:\n", a.sum())
print("tensor a[0]", a[0])
print("tensor a[1]", a[1])

print("tensor[0][1]:\n", a[0][1])   #row: 1, col: 2
print("tensor[0][2]:\n", a[0][2])   #row: 1, col: 3
print("tensor[2][1]:\n", a[2][1])   #row: 3, col: 2

print("torch.sum(a, dim=1)\n", torch.sum(a, dim=0))
print("torch.sum(a, dim=1)\n", torch.sum(a, dim=1))