"""
    ex:
        ta : 2022-02-22 14:37:30.1563
        tb : 2022-02-23 14:38:20.1234
    =>  result : 49.9698 (s)
"""

def msdelta(ta, tb):
    tc = tb - ta
    t = float(str(tc).split(":")[-1])
    print(t)
    return t

import datetime
import time

a = datetime.datetime.now()
time.sleep(60)
b = datetime.datetime.now()

msdelta(a, b)