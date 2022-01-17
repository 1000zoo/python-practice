from openpyxl import Workbook

wb = Workbook()
orig = wb.active
array = []
array.append([1, 2])
array.append([2, 3])
orig.append(array.pop())
orig.append(array.pop())


wb.save('test.xlsx')