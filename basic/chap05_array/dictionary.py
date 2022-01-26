cabinet_ = {3 : "JW", 10 : "MJ", 45 : "GG"}
print(cabinet_[3])
print(cabinet_[10], cabinet_.get(3))
print(cabinet_.get(5))
# print(cabinet_[5])

print(3 in cabinet_)
print("JW" in cabinet_)
print(5 in cabinet_)

cabinet = {"JW" : "971006", "MJ" : "010205"}
print(cabinet)
print(cabinet.get("JW"))
print(cabinet.get("MJ"))

cabinet["JW"] = "1548487"
cabinet["MJ"] = "1144586"
cabinet["JK"] = "1486543"
print(cabinet)

del cabinet["JK"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)