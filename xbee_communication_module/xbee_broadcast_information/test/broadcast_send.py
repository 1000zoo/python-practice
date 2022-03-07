from digi.xbee.devices import *

PORT = 'COM5'
BAUD_RATE = 9600
LANE = "lane2"
VEHICLE_ID = "97가1006"

broadbee = XBeeDevice(PORT, BAUD_RATE)

print("START")

try:
    print("open")
    broadbee.open()
    print("done")
    
    dataToSend = VEHICLE_ID + "/" + LANE
    
    broadbee.send_data_broadcast(dataToSend)
    print("%s to all\n data : %s" % (broadbee.get_64bit_addr(), dataToSend))
    
except InvalidOperatingModeException as err:
    print(err)
    
finally:
    if broadbee is not None and broadbee.is_open():
        broadbee.close()   
    
print('END')