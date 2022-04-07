#####https://wikidocs.net/14597

import numpy as np

a = np.array([[1,2,-1],[3,7,0],[0,4,-1]])
b = a - 3
print(a.T)
print(a.transpose())

[d, v] = np.linalg.eig(a)   #d = eigenvalues, v = vector
print('d', d)
print('v', v)
print('norm', np.linalg.norm(a))
print('cond', np.linalg.cond(a))
print('det', np.linalg.det(a))
print('solve', np.linalg.solve(a, b))