class Something:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPoint(self):
        return (self.x, self.y)    



some = Something(3, 3)
print(some.getPoint())

print('--------------stack------------------')


pointStack = []
print(not pointStack)
print('-------------------')
tempPoint = Something(4, 6)
pointStack.append(tempPoint.getPoint())
tempPoint = Something(3,7)
pointStack.append(tempPoint.getPoint())
print(not pointStack)
topPoint = pointStack[-1]
print(topPoint)
print(pointStack)
print(pointStack.pop())
print(pointStack.pop())