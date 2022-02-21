from digi.xbee.devices import *

xbee = XBeeDevice("COM5", 9600)
def main():
    try:
        xbee.open()
        xbee.add_data_received_callback(rCallback)
        
        input()
        
    except InvalidOperatingModeException as err:
        print(err)
        
    finally:
        xbee.close()

def rCallback(msg):
    data = msg.data.decode()
    print(data)
    print(len(data))
if __name__ == "__main__":
    main() 