import numpy as np

PATH = 'data_files/'
x = np.array([1.1,2.2,3.1])

x1 = x.copy()
np.savetxt(PATH + 'x1_.txt', x1)

x2 = x.copy().reshape(1, 3)
np.savetxt(PATH + 'x2_.txt', x2)

x3 = x.copy().reshape(3,1)
np.savetxt(PATH + 'x3_.txt', x3)

print(np.loadtxt(PATH + 'x1_.txt'))
print(np.loadtxt(PATH + 'x2_.txt'))
print(np.loadtxt(PATH + 'x3_.txt'))