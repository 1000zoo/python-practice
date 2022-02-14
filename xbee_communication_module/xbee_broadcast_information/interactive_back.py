from charset_normalizer import detect
from digi.xbee.devices import *
from datetime import datetime

PORT = 'COM5'
BAUD_RATE = 9600

LANE = "lane2"          #주행 차선
VEHICLE_ID = "97가1006" #차량 번호
WEB_ADDRESS = "IDK"
DETECTED = True         #차량 감지

#main
def main():
    global isCallbackOn
    global userInfo
    global broadbee
    isCallbackOn = False
    print("========== MAIN==========")
    print("==========START==========")
    broadbee = XBeeDevice(PORT, BAUD_RATE)
    userInfo = init_user()
    
    try:
        broadbee.open()
        on = True
    except InvalidOperatingModeException as err:
        print(err)
        on = False

    while on:
        if not isCallbackOn:
            broadbee.add_data_received_callback(data_receive_callback)
            isCallbackOn = True

        if is_detected():
            data_broadcast(broadbee.get_node_id())
        else:
            print(("not dectected..."))
        input()

    print("end of the function")


#감지 확인 함수, 감지 여부에 따라 True, False 리턴
def is_detected():
    return DETECTED

#수신용 callback 함수
def data_receive_callback(xbee_message):
    print("\n\n")
    print("==========DATA==========")
    print("======== RECEIVE========")
    print("========CALLBACK========")
    print("data receiving...")
    dataReceived = xbee_message.data.decode().split("/")
    lane = dataReceived[0]
    print("lane checking...")
    print(dataReceived)
    if lane == userInfo[0]:
        print("same lane")
        if not is_detected():
            data_send_reactive(dataReceived)
    else:
        print("diff lane")
        print(lane, userInfo[0])
    isCallbackOn = False

#감지 시 송신용 함수
def data_broadcast(nodeId):
    print("\n\n")
    print("==========DATA==========")
    print("======= BROADCAST=======")
    dataToSend = userInfo[0] + "/" + userInfo[1] + "/" + nodeId
    broadbee.send_data_broadcast(dataToSend)

#수신 시 송신용 함수
def data_send_reactive(data):
    print("\n\n")
    print("==========DATA==========")
    print("==========SEND==========")
    print("========REACTIVE========")
    print("reacting to %s" % data[2])
    net = broadbee.get_network()
    reac = net.discover_device(data[2])
    dataToSend = userInfo[0] + "/" + userInfo[1] + "/" + broadbee.get_node_id()
    broadbee.send_data(reac, dataToSend)
    print("success")

#사용자 정보를 초기화 해주는 함수
def init_user():
    print("\n\n")
    print("==========INIT==========")
    print("==========USER==========")
    return LANE, VEHICLE_ID

if __name__ == '__main__':
    main()