a = "A"
b = "B"
c = "C"
d = "D"

alp = {}

alp["a"] = a
alp["b"] = b
alp["c"] = c
alp["d"] = d

k = str(alp)
print(k)
k = k.strip("{""}")
print(k)
ls = k.split(",")
print(ls)

dic = {}
for w in ls:
    w = w.split(":")
    k = w[1].lstrip()
    dic[w[0].strip(" '")] = w[1].strip(" '")

print(dic)
print(dic["a"])
print(dic["b"])
print(dic["c"])
print(dic["d"])