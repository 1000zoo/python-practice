#####https://wikidocs.net/33275

import numpy as np

x = np.array([1,2,3], dtype=np.int16)
xf = np.array([1,2,3], dtype='float64')

print("x.dtype==np.int16 => ", x.dtype==np.int16)
print(type(xf))