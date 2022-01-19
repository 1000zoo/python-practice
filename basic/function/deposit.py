def deposit(balance, money):
    total = balance + money
    print("It's done. Your balance is {0}$.".format(total))
    return total

balance = 0
balance = deposit(balance, 1000)
print(balance)