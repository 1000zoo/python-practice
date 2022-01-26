print("-"*25 + "local" + "-"*25)
gun = 10

def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print("[In function]: left gun: {0}.".format(gun))

print("gun: {0}".format(gun))
checkpoint(2)
print("left: {0}".format(gun))

print("-"*25 + "global" + "-"*25)

food = 10

def checkpoint(soldiers):
    global food
    food = food - soldiers
    print("[In function]: left food: {0}.".format(food))

print("food: {0}".format(food))
checkpoint(2)
print("left: {0}".format(food))