try:
    num = []
    num.append(int(input("num1: ")))
    num.append(int(input("num2: ")))
    print(str(num[1]/num[2]))
except ValueError as err:
    print("ValueError!", err)
except ZeroDivisionError as err:
    print("ZeroDivisionError!", err)
except Exception as err:
    print("???", err)
    
print("After try/except")
