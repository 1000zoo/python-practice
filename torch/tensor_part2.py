import torch

b = torch.arange(3*3*3).view(3,3,3)

print("torch 3X3X3:\n", b)
# print("torch[0]:\n", b[0])
# print("torch[0][1]:\n", b[0][1])
# print("torch[0][1][2]:\n", b[0][1][2])

print("torch.sum(b,dim=0):\n", torch.sum(b, dim=0))
print("torch.sum(b,dim=1):\n", torch.sum(b, dim=1))
print("torch.sum(b,dim=2):\n", torch.sum(b, dim=2))
print("torch.sum(b, 0)\n", torch.sum(b, 0))
print("torch.sum(b, (0,1))\n", torch.sum(b, (0,1)))
print("torch.sum(b, (0,1,2))\n", torch.sum(b, (0,1,2)))
