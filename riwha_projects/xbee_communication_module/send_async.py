from digi.xbee import xsocket
from digi.xbee.devices import CellularDevice
from digi.xbee.models.protocol import IPProtocol

# Create and open an XBee Cellular.
xbee = CellularDevice("COM6", 9600)
xbee.open()

# Create a new XBee socket.
sock = xsocket.socket(xbee, IPProtocol.TCP)