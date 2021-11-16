from haversine import haversine
from openpyxl import Workbook

class Point:
    def __init__ (self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

midExcel = Workbook()
m = midExcel.active

midPoints = []
pointStack =[]

start = Point(36.63533335,	127.3185)
goal = Point(36.63483333,	127.3211667)

pointStack.append(goal)

current = start

while not not pointStack:
    temp = pointStack[-1]
    s = (current.latitude, current.longitude)
    g = (temp.latitude, temp.longitude)
    if haversine(s, g, unit='m') >= 0.8:
        midLat = (current.latitude + temp.latitude) / 2
        midLon = (current.longitude + temp.longitude) / 2
        currentMidpoint = Point(midLat, midLon)
        pointStack.append(currentMidpoint)
    else:
        print(current.latitude, current.longitude)
        m.append([current.latitude, current.longitude])
        # midPoints.append(current)
        current = pointStack.pop()

# midPoints.append(current)
# print(midPoints)

midExcel.save('Midpoints.xlsx')
