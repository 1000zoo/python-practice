#####https://wikidocs.net/14606

import numpy as np

# shape 변경
x = np.arange(0, 24, 1.0)
print(x)
print(x.dtype)

w = x.reshape((2,12))
y = x.reshape((2,3,4))
z = x.reshape((4,6))
k = z.reshape((z.size,))
print(w)
print(y)
print(z)
print(k)
print('-'*30)


# dtype 변경
z.astype(np.float32)
print(z)
print(z.dtype)