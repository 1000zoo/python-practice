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

#5-2 중반부분부터