from digi.xbee.devices import XBeeDevice
import time

PORT = "COM6"
BAUD_RATE = 9600


def main():
    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

            
        device.add_data_received_callback(data_receive_callback)

        while True:
            print("waiting...")
            time.sleep(10)

    finally:
        if device is not None and device.is_open():
            device.close()

def data_receive_callback(xbee_message):
    # print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
    #                          xbee_message.data.decode()))
    dataReceived = xbee_message.data.decode().split("/")
    print("lane : %s" % dataReceived[0])
    print("car id : %s" % dataReceived[1])
    print("MAC : %s" % xbee_message.remote_device.get_64bit_addr())
    print("ID : %s" % xbee_message.remote_device.get_node_id())

if __name__ == '__main__':
    main()