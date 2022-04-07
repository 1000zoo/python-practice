#####https://wikidocs.net/14597

import numpy as np

a = np.arange(9).reshape(3, 3)
b = np.arange(11, 20).reshape(3, 3)
print(a, '\n', b)
print('='*30)

x = np.arange(3)
y = np.arange(3).reshape(3, 1)
z = np.arange(3).reshape(1, 3)
print(x, '\n', y, '\n', z)
print('='*30)

c1 = np.dot(a, b)
c2 = np.matmul(a, b)
c3 = a@b
print(c1, '\n', c2, '\n', c3)
print('='*30)

ax1 = np.dot(a, x)
ax2 = np.matmul(a, x)
ax3 = a@x
print(ax1, '\n', ax2, '\n', ax3)
print('='*30)

ay1 = np.dot(a, y)
ay2 = np.matmul(a, y)
ay3 = a@y
print(ay1, '\n', ay2, '\n', ay3)
print('='*30)

#error
# az1 = np.dot(a, z)
# az2 = np.matmul(a, z)
# az3 = a@z
# print(az1, '\n', az2, '\n', az3)
# print('='*30)

print(x@y)