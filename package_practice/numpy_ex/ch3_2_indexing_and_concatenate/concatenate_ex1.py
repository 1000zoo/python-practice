#####https://wikidocs.net/14607

import numpy as np

a = np.array([[1,2], [3,4]])
b = np.array([[5,6]])
c = np.concatenate((a, b), axis=0)
print(a)
print(b)
print(c)

x = np.array([1,2,3])
y = np.array([4,5,6])
z1 = np.vstack((x, y))
z2 = np.hstack((x, y))
z3 = np.append(x, y)
print('z1')
print(z1)
print('z2')
print(z2)
print('z3')
print(z3)