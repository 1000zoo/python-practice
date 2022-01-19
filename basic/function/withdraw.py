def  withdraw(balance, money):
    if balance >= money:
        total = balance - money
        print("It's done. Your balance is {0}$.".format(total))
        return total
    else:
        print("Your balance is less than {0}.\nYour balance is {1}.".format(money, balance))
        return balance
    
balance = 1000
balance = withdraw(balance, 800)
balance = withdraw(balance, 800)
print(balance)
    