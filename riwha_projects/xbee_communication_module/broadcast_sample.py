from digi.xbee.devices import *

PORT = 'COM5'
BAUD_RATE = 9600

DATA_TO_SEND = "ON AIR"

broadbee = XBeeDevice(PORT, BAUD_RATE)

print("START")

try:
    print("open")
    broadbee.open()
    print("done")
    
    broadbee.send_data_broadcast(DATA_TO_SEND)
    print("%s to all" % broadbee.get_64bit_addr())
    
except InvalidOperatingModeException as err:
    print(err)
    
finally:
    if broadbee is not None and broadbee.is_open():
        broadbee.close()   
    
print('END')