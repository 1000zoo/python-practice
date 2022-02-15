k = [1,2,3,4,5,0,3,5,6,0,3]
i = 0
try:
    while i < 20:
        i += 1
        print(5/k[i])
except ZeroDivisionError as err:
    print(err)
finally:
    print("hhh")