#####https://wikidocs.net/14632

import numpy as np

a = [1,2,3]
x = np.array(a)
y = x
y[0] = 10       # => 복사한 값(x) 까지 변경
print('a', a)
print('x', x)  
print('y', y)

print(y is x)
z = x.copy()    # deep copy -> 값 자체만 복사, 주소값 복사 X
print(z is x)
z[0] = 4
print('x', x)
print('z', z)