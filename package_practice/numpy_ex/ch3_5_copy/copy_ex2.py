#####https://wikidocs.net/14632

import numpy as np

x = np.array([1,2,3])
y = x[0:2]              #  slicing 할 때 역시 복사된 값(x) 도 바뀜
y[0] = 10

print('x', x)
print('y', y)

a = np.array([4,5,6])
b = a[0:2].copy()
b[0] = -43
print('a', a)
print('b', b)