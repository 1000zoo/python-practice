from digi.xbee.devices import *

xbee = XBeeDevice("COM5", 9600)
xbee.open(force_settings=True)

xbee_message = xbee.read_data(10)
print(xbee_message.data)
