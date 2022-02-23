import datetime
import time

TIME_ZERO = datetime.datetime.strptime("00:00:00", "%H:%M:%S")

a = datetime.datetime.now()
print(a)
time.sleep(0.5)
b = datetime.datetime.now()
print(b)
print(b-a)
print(str(b-a))
k = str(b-a).split(":")
print(k[-1])