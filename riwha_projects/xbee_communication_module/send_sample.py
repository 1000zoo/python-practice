from digi.xbee.devices import *
from serial import SerialException

PORT = "COM6"
BAUD_RATE = 9600

xbee = XBeeDevice(PORT, BAUD_RATE)

try:    
    xbee.open(force_settings=True)
    remote = RemoteXBeeDevice(xbee, XBee64BitAddress.from_hex_string("0013A2004182D651"))
    xbee.send_data(remote, "Hello XBee!")
    
except InvalidOperatingModeException as err:
    print(err) 
    
except SerialException as err:
    print(err)

finally:
    if xbee is not None and xbee.is_open():
        print("done")
        xbee.close()
    else:
        print("fail")
        