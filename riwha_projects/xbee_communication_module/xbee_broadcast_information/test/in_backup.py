from digi.xbee.devices import *
from datetime import datetime
import interface

PORT = 'COM5'
BAUD_RATE = 9600

VEHICLE_ID = "97가1006" #차량 번호

LANE = "lane2"          #주행 차선
DETECTED = True         #차량 감지
GPS = (36.156464184744, 127.333554684111)

#main
def main():
    global isCallbackOn
    global userInfo
    global broadbee
    interface.main_if()
    userInfo = {}
    broadbee = XBeeDevice(PORT, BAUD_RATE)
    isCallbackOn = False

    while True:  
        try:
            broadbee.open()
            init_user()
            lane_check()
            if not isCallbackOn:
                broadbee.add_data_received_callback(data_receive_callback)
                isCallbackOn = True

            if is_detected():
                gps_update()
                data_broadcast()
                
            else:
                print("not dectected...")
            time.sleep(2)
            print("end of the function")
                
        except InvalidOperatingModeException as err:
            print(err)

def lane_check():
    userInfo["lane"] = LANE

def gps_update():
    userInfo["GPS"] = GPS

def init_user():
    ui = {
        "vehicleId" : VEHICLE_ID,
        "nodeId" : broadbee.get_node_id(),
    }
    return ui

def is_detected():
    return DETECTED

def data_receive_callback(xbee_message):
    global isCallbackOn
    
    isCallbackOn = True
    interface.data_receive_callback_if()
    dataReceived = string_to_dict(xbee_message.data.decode())
    print(datetime.now())
    print(dataReceived)
    
    try:
        if dataReceived["lane"] == userInfo["lane"]:
            print("same lane")
            print("gps: %s" % dataReceived["GPS"])  #gps 정보 처리 추가
            data_send_reactive(dataReceived)
        else:
            print("diff lane")
            print(dataReceived["lane"], userInfo["lane"])
    except KeyError as err:
        if err == "'GPS'":
            pass
        else:
            print("Key '%s' does not exist in data" % err)

def data_send_reactive(data):
    interface.data_send_reactive_if()
    print("reacting to %s" % data["nodeId"])
    net = broadbee.get_network()
    reac = net.discover_device(data["nodeId"])
    broadbee.send_data(reac, str(userInfo))

def data_broadcast():
    interface.data_braodcast_if()
    broadbee.send_data_broadcast(str(userInfo))

def string_to_dict(s):
    dic = {}
    s = s.strip("{""}")
    ls = s.split(",")
    for w in ls:
        try:    
            w = w.split(":")
            dic[w[0].strip(" '")] = w[1].strip(" '")
        except IndexError as err:
            print(err)
            return
    return dic

if __name__ == '__main__':
    main()