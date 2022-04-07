#####https://wikidocs.net/14597

import numpy as np

# sort

x = np.array([9.1,8.2,2.3,5,6.3,6.7,1.3])
print('amin', np.amin(x))
print('x.min', x.min)
y = np.sort(x)
print('y', y)
# x.sort() => return 없음
print(np.argsort(x)) # 정렬했을 때 인덱스
print(x[np.argsort(x)[-2]])

# binary search

x = np.array([0, 12, 26, 30])

# side='left' => array[i-1] < value <= 'array[i]'
# side='right' => array[i-1] <= value < 'array[i]'
print(x)
print('-1: ', np.searchsorted(x, -1.), np.searchsorted(x, -1., side='right'))
print('0: ', np.searchsorted(x, 0.), np.searchsorted(x, 0., side='right'))
print('5: ', np.searchsorted(x, 5.), np.searchsorted(x, 5., side='right'))
print('13: ', np.searchsorted(x, 13.), np.searchsorted(x, 13., side='right'))
print('15: ', np.searchsorted(x, 15.), np.searchsorted(x, 15., side='right'))
print('30: ', np.searchsorted(x, 30.), np.searchsorted(x, 30., side='right'))