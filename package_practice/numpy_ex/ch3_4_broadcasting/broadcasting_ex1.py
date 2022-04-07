#####https://wikidocs.net/14608

import numpy as np

a = np.arange(9.).reshape(3, 3)
x = np.array([1., 0, 0])
y = x.reshape(1, 3)
z = x.reshape(3, 1)
print('a\n', a)
print('x\n', x)
print('y\n', y)
print('z\n', z)

print('a+1\n', a+1)
print('a+x\n', a+x)
print('a+y\n', a+y)
print('a+z\n', a+z)
print('y+z\n', y+z)