from digi.xbee.devices import *

xbee = XBeeDevice("COM6", 9600)
m1 = "helloadfaevwaevfawegfreawgrdasdfewqdfggaaaewqfawvllafdavcaedf1818k189181980000015..19815848484rewqr:!@#"
m2 = "my"
try:
    xbee.open()
    xbee.send_data_broadcast(m1)
    
except InvalidOperatingModeException as err:
    print(err)
    
finally:
    xbee.close()