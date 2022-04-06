#####https://wikidocs.net/14607

import numpy as np

a = np.arange(10, 20, 1)
print(a[0])
print(a[-1])
print(a[0:-1])
print(a[:])

# 인덱스 배열
idx = [0,2,4,6,8]
print(a[idx])

# boolean 배열
x = np.linspace(-5, 5, 11)
print(x > 3)
idx = x < -3
print(idx)
print(x[idx])
boolean = [True, False, True, False, False, True, False, True, False, False, False]
print(x[boolean])