import schedule as sc

def printname(name):
    print(name, "Hello!")

sc.every(10).seconds.do(printname, "JW")

sc.run_pending()