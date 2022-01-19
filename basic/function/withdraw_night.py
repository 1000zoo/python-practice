def withdraw_night(balance,  money):
    commission = 3
    print("commision: {0}, Your balance is {1}".format(commission, balance - money - commission))
    return commission, balance - money - commission

balance = 1000
commision, balance = withdraw_night(balance, 100)
print(commision, balance)
