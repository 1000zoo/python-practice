#####https://wikidocs.net/14612

import numpy as np

x = np.arange(9).reshape(3, 3)
np.savetxt('data_files/3x3.txt', x)

y = np.loadtxt('data_files/3x3.txt')
print(y)