students = [1,2,3,4,5]
print(students)

students = [i + 100 for i in students]
print(students)

re = [x - 100 for x in students]
print(re)

name = ["Weekend", "Drake", "Miller", "Rihanna"]
name_len = [len(l) for l in name]
print(name_len)

name_upper = [u.upper() for u in name]
print(name_upper)