try:
    print("Only Integer.")
    num1 = (input("num1: "))
    num2 = (input("num2: "))
    if type(num1) != int or type(num2) != int:
        raise ValueError
    print(str(num1/num2))
    
except ValueError:
    print("Only Integer!!")