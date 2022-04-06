#####https://wikidocs.net/14606


import numpy as np

#ndarray 초기화 관련 함수
x = np.zeros((3,3))
y = np.ones((3,3), dtype='int32')
z = np.empty((3,3), dtype='int32')
print(x)
print(y)
print(z)
print('-'*30)

#null list 로 초기화 후 append 로 추가
w = np.array([])
for i in range(3):
    w = np.append(w, [1,2,3])
print(w)
print('-'*30)

# arrange(from, to, step)
a = np.arange(1, 2, 0.1)
b = np.arange(10)
c = np.arange(10.0)
print(a)
print(b)
print(c)
print('-'*30)

# linspace(from, to. npoints), eye(root(size))
l1 = np.linspace(0., 30., 21)
l2 = np.linspace(0., 1.0, 21)
e = np.eye(4)
print(l1)
print(l2)
print(e)