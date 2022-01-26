class TypeError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg

try:
    print("Only Integer.")
    num1 = (input("num1: "))
    num2 = (input("num2: "))
    if type(num1) != int or type(num2) != int:
        raise TypeError("Input must be Integer!!")
    print(str(num1/num2))
    
except TypeError as err:
    print("Only Integer!!")
    print(err)
    
finally:
    print("end")