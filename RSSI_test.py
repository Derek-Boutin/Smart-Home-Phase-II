import socket
import requests
import json
import threading


def deviceController(command):
    topLevelUrl = 'http://127.0.0.1:8083'
    LoginUrl = topLevelUrl + '/ZAutomation/api/v1/login'
    username = 'admin'
    password = 'laurensellers'

    LoginHeader = {'User-Agent': 'Mozilla/5.0', 'Cotent-Type': 'application/json'}
    Formlogin = '{"form": true, "login": "'+username+'", "password": "'+password+'", "keepme": false, "default_ui": 1}'

    session = requests.Session()
    session.post(LoginUrl, headers=LoginHeader, data=Formlogin)

    RequestUrl = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_3-0-38/command/' + command
    response = session.get(RequestUrl)
    print(response)


def clientConn(name, conn):
    global i
    global RSSI_1
    global RSSI_2
    
    ID = conn.recv(10).decode('UTF-8')
    rssi = conn.recv(50).decode('UTF-8')
    
    if (str(ID) == '1'):
        
        RSSI_1 = rssi
    elif (str(ID) == '2'):
        
        RSSI_2 = rssi
    
    print("I " + str(i))
    print("ID " + str(ID))
    print("RSSI " + str(rssi))
    i += 1
    conn.close()


def sensor_module_conn():
    port = 4000 # port number
    host = '192.168.1.2' #ip address of hub

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket
    s.bind((host, port)) 

    s.listen(5) #listen for max 5 connections
    print("Hub listening....")
    print(threading.active_count())
    while True:
        client, address = s.accept()
        print("Connecting with " + str(address))

        t = threading.Thread(target=clientConn, args=("clientThread", client))
        t.start()

        

i = 0
RSSI_1 = 0
RSSI_2 = 0
conn = threading.Thread(target=sensor_module_conn)
conn.start()

while True:
    if (i == 2):
        RSSI_1_int = int(RSSI_1)
        RSSI_2_int = int(RSSI_2)
        print("Hello World")
        if (RSSI_1_int > RSSI_2_int):
            print("on")
            deviceController('on')
        elif (RSSI_2_int > RSSI_1_int):
            print("off")
            deviceController('off')
        i = 0









            
