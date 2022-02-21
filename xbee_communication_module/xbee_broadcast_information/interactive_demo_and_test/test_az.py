import math
import numpy

def Azimuth(lat1, lng1, lat2, lng2):
    Lat1 = math.radians(lat1)
    Lng1 = math.radians(lng1)
    Lat2 = math.radians(lat2)
    Lng2 = math.radians(lng2)
    
    y = math.sin(Lng2 - Lng1) * math.cos(Lat2)
    x = math.cos(Lat1) * math.sin(Lat2) - math.sin(Lat1) * \
        math.cos(Lat2) * math.cos(Lng2 - Lng1)
    z = math.atan2(y, x)
    
    a = numpy.rad2deg(z)
    if(a < 0):
        a = 180 + (180 + a)
    return a

print(Azimuth(36.1230103200, 123.53200123000, 36.12320100012, 123.5321500000))
print(Azimuth(36.12320100012, 123.5321500000, 36.1230103200, 123.53200123000))