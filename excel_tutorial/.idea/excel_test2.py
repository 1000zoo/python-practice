from openpyxl import Workbook

file = Workbook()
k = file.active

toAppend = []

toAppend.append([1,2])
toAppend.append([2,3])
toAppend.append([3,4])

for i in toAppend:
    k.append(i)

file.save("test2.xlsx")
