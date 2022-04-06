import schedule as sc
import datetime

def printtime(now):
    print(now, "\nHello!")

sc.every(10).seconds.do(printtime, str(datetime.datetime.now()))

while True:
    sc.run_pending()