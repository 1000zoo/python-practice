mySet = {1,2,3,3,3}
print(mySet)

print("-"*75)

T1 = {"Faker", "GumaYusi", "Zeus", "Someone"}
GenG = set(["Ruler", "Chovy", "Peanut", "Someone"])

#And
print(T1 & GenG)
print(T1.intersection(GenG))

print("-"*75)

#Or
print(T1 | GenG)
print(T1.union(GenG))

print("-"*75)

#Difference
print(T1 - GenG)
print(T1.difference(GenG))

print("-"*75)

T1.add("Teddy(ex)")
print(T1)
T1.remove("Teddy(ex)")
print(T1)