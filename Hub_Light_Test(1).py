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

#RequestUrl = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/update' #Updates light level from dashboard
#response = session.get(RequestUrl)
#response = session.get(RequestUrl) #Called a second time to send it back to be outputted in the shell
#print(response)

#RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
#response = session.get(RequestUrl_1)
#print(response)

#r = session.put(RequestUrl_1)
#res = json.loads(response.text)
#print(res)
#print(res['data']['metrics']['level'])
#level = res['data']['metrics']['level']
#print(json.dumps(res, indent=4))

#light_data = open("Light Data (2).txt", "a")
#light_data.write("Light Level Data\n")
#light_data.close()


port = 4000 # port number
host = '192.168.1.23' #ip address of hub
old_message = 0
old_level = 0
original_light_level = 0
i = 0
j = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket
s.bind((host, port)) 

s.listen(5) #listen for max 5 connections
print("Hub listening....")

while True:
    client, address = s.accept()
    print("Connecting with " + str(address))
    while client:
        message = client.recv(1024).decode('UTF-8')
        #int_message = int(message)
        print(message + "lux")
        if (message == old_message):
            i = i + 1
            #j = j + int_message
            if (i==3):
                RequestUrl = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/update' #Updates light level from dashboard
                response = session.get(RequestUrl)
                response = session.get(RequestUrl) #Called a second time to send it back to be outputted in the shell
                RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                response = session.get(RequestUrl_1)
                r = session.put(RequestUrl_1)
                res = json.loads(response.text)
                new_level = res['data']['metrics']['level']
                if (new_level!=old_level):
                    light_data = open("Light Data.txt", "a")
                    #avg_light_level = int_message/5
                    str_original_light_level = str(original_light_level)
                    light_data.write(str_original_light_level+ "\n") #x-coordinate
                    string_level = str(new_level)
                    light_data.write(string_level + "\n") #y-coorindate
                    light_data.close()
                    #The first line of this file is the original light level (x-coordinate)
                    #The second line of this file is the dim level (y-coordinate)
                    #This pattern repeats throughout 
                    old_level = new_level
                    #End of if statement
                    
                original_light_level = message
                i=0
        else:
            i=0
        old_message = message   

