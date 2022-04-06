from digi.xbee.devices import *

xb = XBeeDevice("COM5", 9600)
xb.open()

print(xb.read_device_info(init=True))
xb.set_node_id("BACK")