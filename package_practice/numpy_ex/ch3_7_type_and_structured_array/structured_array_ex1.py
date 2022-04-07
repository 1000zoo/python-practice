####https://wikidocs.net/33275

from unicodedata import name
import numpy as np

dtype = [('name', 'S10'), ('age', 'int32'), ('height', 'float64')]      # int32 = <i4 / float64 = <f4
x = np.array([('Alice', 19, 173.), ('Bob', 20, '181.')], dtype=dtype)
print(x)
print(x.dtype)
print(x.shape)

print('x[name]', x['name'], 'x[age]', x['age'])
print('x[0]: ', x[0], 'x[-1]:', x[-1])

y = np.zeros(3, dtype=dtype)
print('y before : ', y)

y['name'] = ['JW', 'MJ', 'PP']
y['age'] = [26, 22, 22]
y['height'] = [173., 164., 170.]
print('y after : ', y)