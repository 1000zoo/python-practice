from random import *

count = 0
for passenger in range(1,51):
    t = randrange(5, 51)
    if t >= 5 and t <= 15:
        print("[O] no.{0} passenger : (time : {1}).".format(passenger, t))
        count += 1
    else:
        print("[X] no.{0} passenger : (time : {1}).".format(passenger, t))
        
print("total : {0}".format(count))