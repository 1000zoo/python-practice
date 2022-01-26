chicken = 10
waiting = 1

class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg
    
while(True):
    print("남은 치킨: {0}".format(chicken))
    try:
        order = int(input("몇마리? > "))
        if order > chicken:
            raise SoldOutError("Sold Out")
        elif order <= 0:
            raise ValueError("양수만")
        else:
            print("주문 완료")
            waiting += 1
            chicken -= order
    except ValueError as err:
        print(err)
    except SoldOutError as err:
        print(err)
        break
        
    
