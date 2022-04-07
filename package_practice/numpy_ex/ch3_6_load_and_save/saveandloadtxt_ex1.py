#####https://wikidocs.net/14612

import numpy as np

PATH = 'data_files/'

x1 = np.array([1.1,2.2,3.1])
np.savetxt(PATH + 'x1.txt', x1)

x2 = np.array([1.1,2.2,3.1]).reshape(1, 3)
np.savetxt(PATH + 'x2.txt', x2)

x3 = np.array([1.1, 2.2, 3.1]).reshape(3,1)
np.savetxt(PATH + 'x3.txt', x3)

print(np.loadtxt(PATH + 'x1.txt'))
print(np.loadtxt(PATH + 'x2.txt'))
print(np.loadtxt(PATH + 'x3.txt'))