import schedule as sc

def printname(name):
    print(name, "Hello!")

sc.every(10).seconds.do(printname, "JW")

while True:
    sc.run_pending()