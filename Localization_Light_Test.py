import socket
import requests
import json

topLevelUrl = 'http://192.168.1.23:8083'
LoginUrl = topLevelUrl + '/ZAutomation/api/v1/login'
username = 'admin'
password = 'laurensellers'

LoginHeader = {'User-Agent': 'Mozilla/5.0', 'Cotent-Type': 'application/json'}
Formlogin = '{"form": true, "login": "'+username+'", "password": "'+password+'", "keepme": false, "default_ui": 1}'

session = requests.Session()
session.post(LoginUrl, headers=LoginHeader, data=Formlogin)

port_1 = 4000 # hub to esp32 port number
port_2 = 6000 # cloud to hub port number
host = '192.168.1.23' #ip address of hub
sensing = '192.168.1.25' #ip address of sensing module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket
s.bind((host, port_1))
#s.bind((host, port_1))

level = 0
RequestUrl_on = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/on' #+ level
RequestUrl_off = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/off'

#response = session.get(RequestUrl_off)
#print(response)
#r = session.get(RequestUrl_on)

s.listen(5) #listen for max 5 connections
print("Hub listening....")

#handles only output from cloud 
while True:
    client, address = s.accept()
    print("Connecting with " + str(address))
    room = client.recv(1024).decode('UTF-8')
    #int_message = int(message)
    print(room)
    if (room == 'extra-room'):
        #response = session.get(RequestUrl_on)
        r = session.get(RequestUrl_on)
        print(r)
    else:
        #response = session.get(RequestUrl_off)
        r = session.get(RequestUrl_off)
        print(r)
        
    client.close()
