import datetime
import time

a = datetime.datetime.now()
# b = a - datetime.timedelta(days=1)
time.sleep(1)
b = datetime.datetime.now()


print(a)
print(b)
c = (b-a)
c.microseconds
s = str(c).split(":")[-1]
print(c)
print(s)
print(float(s))