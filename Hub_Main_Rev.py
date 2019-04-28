import socket
import requests
import json
import threading
import mysql.connector
import json
import numpy as np
from math import sqrt
from collections import Counter

def clientConn(name, conn):
    global RSSI_1
    global RSSI_2
    global RSSI_3
    global ID1
    global ID2
    global ID3
    global light1
    global light2
    global light3
    ID = conn.recv(1).decode('UTF-8')
    rssi = conn.recv(3).decode('UTF-8')
    light_level = conn.recv(10).decode('UTF-8')
    if (str(ID) == '1'):
        RSSI_1 = rssi
        light1 = light_level
        ID1 = True
        #print("1 " + str(ID1))
        print(str(ID) + "   " + str(rssi))

    elif (str(ID) == '2'):
        RSSI_2 = rssi
        light2 = light_level
        ID2 = True
        print(str(ID) + "   " + str(rssi))

    elif (str(ID) == '3'):
        RSSI_3 = rssi
        light3 = light_level
        ID3 = True
        print(str(ID) + "   " + str(rssi))


def sensor_module_conn():
    port = 4000 # port number
    host = '192.168.1.23' #ip address of hub
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket
    s.bind((host, port)) 
    s.listen(5) #listen for max 5 connections
    print("Hub listening....")
    print(threading.active_count())
    while True:
        client, address = s.accept()
        address = str(address)
        print("Connecting with " + str(address))
        t = threading.Thread(target=clientConn, args=("clientThread", client))
        #print(threading.active_count())
        t.start()

def CloudConn(name, data):
    port = 6000
    address = '192.168.1.30'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))
    s.sendall(data.encode('utf-8'))
    output = s.recv(1024).decode('utf-8')
    output = json.loads(output)
    s.close()
    float_output = float(output)
    int_output = int(float_output)
    #light_control(output,room) #Need to separate these two data entries sent from the cloud
    str_output = str(int_output)
    print("Output:" + str_output)
    light_control(str_output)
    
def light_control(level):
    topLevelUrl = 'http://192.168.1.23:8083'
    LoginUrl = topLevelUrl + '/ZAutomation/api/v1/login'
    username = 'admin'
    password = 'laurensellers'
    LoginHeader = {'User-Agent': 'Mozilla/5.0', 'Cotent-Type': 'application/json'}
    Formlogin = '{"form": true, "login": "'+username+'", "password": "'+password+'", "keepme": false, "default_ui": 1}'
    session = requests.Session()
    session.post(LoginUrl, headers=LoginHeader, data=Formlogin)
    RequestUrl_on_extra_room = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/exact?level=' + level
    r = session.get(RequestUrl_on_extra_room)
    #Need to know how to receive the predicted room to use as a parameter in this function
    '''
    if (room == 'extra-room'):
        RequestUrl_on_extra_room = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/?=' + level
        r = session.get(RequestUrl_on_extra_room)
        
    if (room == 'bed-room'):
        RequestUrl_on_bed_room = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/?=' + level #Need to change ID of switch
        r = session.get(RequestUrl_on_bed_room)
        
    if (room == 'living-room'):
        RequestUrl_on_bed_room = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/?=' + level #Need to change ID of switch
        r = session.get(RequestUrl_on_living_room)
    '''

ID1 = False
ID2 = False
ID3 = False
RSSI_1 = 0
RSSI_2 = 0
RSSI_3 = 0 
light1 = 0
light2 = 0
light3 = 0
conn = threading.Thread(target=sensor_module_conn)
conn.start()
k = 3

while True:
    if (ID1 == True and ID2 == True and ID3 == True):
        #print(dataset)
        new_RSSI = []
        data1 = {"ID": 1, "RSSI": RSSI_1, "light_level": light1}
        data2 = {"ID": 2, "RSSI": RSSI_2, "light_level": light2}
        data3 = {"ID": 3, "RSSI": RSSI_3, "light_level": light3}
        dataToSend = []
        dataToSend.append(data1)
        dataToSend.append(data2)
        dataToSend.append(data3)
        jsonData = json.dumps(dataToSend)
        Cloud = threading.Thread(target=CloudConn, args=("Send to Cloud", jsonData))
        Cloud.start()
        del new_RSSI[:]
        ID1 = False
        ID2 = False
        ID3 = False