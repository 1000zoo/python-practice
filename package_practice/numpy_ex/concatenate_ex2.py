import numpy as np

a = np.array([[1,2,3], [4,5,6]])
b = np.array([[7,8,9]])
c = np.concatenate((a, b), axis=0)
print(c)
print('-'*30)
x = np.array([[1,2,3,4], [5,6,7,8]])
y = x + 1
z1 = np.concatenate((x, y), axis=0)
z2 = np.concatenate((x, y), axis=1)
print(x)
print(y)
print('-'*30)
print(z1)
print('-'*30)
print(z2)