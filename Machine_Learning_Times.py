import time
import datetime
from datetime import timedelta    
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

old_message = 0
old_level = 0
original_light_level = 0
i = 0
j = 0

start_time = datetime.datetime.now()
print(start_time)

updated_time = start_time #Initalize the updated_time variable
updated_time_days = " "
updated_time_days_int = 0
end_time = start_time + timedelta(days=7)
print(end_time)
#print(updated_time_days)

time_hours = start_time.strftime("%H")
time_hours_int = int(time_hours)
print(time_hours)

end_time_days = end_time.strftime("%d")
end_time_days_int = int(end_time_days)
print(end_time_days_int)

      
#print(seconds)

port = 4000 # port number
host = '192.168.1.23' #ip address of hub

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket
s.bind((host, port)) 

s.listen(5) #listen for max 5 connections
print("Hub listening....")

while True:
    client, address = s.accept()
    print("Connecting with " + str(address))
    while client:

        while (updated_time_days_int < (end_time_days_int-1)):
            if (time_hours_int == 0):
                print("yes")
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
                            light_data = open("Light Data 0.txt", "a")
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
                
            elif (time_hours_int == 1):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 1.txt", "a")
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

            elif (time_hours_int == 2):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 2.txt", "a")
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

            elif (time_hours_int == 3):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 3.txt", "a")
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

            elif (time_hours_int == 4):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 4.txt", "a")
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

            elif (time_hours_int == 5):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 5.txt", "a")
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

            elif (time_hours_int == 6):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 6.txt", "a")
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

            elif (time_hours_int == 7):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 7.txt", "a")
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

            elif (time_hours_int == 8):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 8.txt", "a")
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

            elif (time_hours_int == 9):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 9.txt", "a")
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

            elif (time_hours_int == 10):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 10.txt", "a")
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

            elif (time_hours_int == 11):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 11.txt", "a")
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

            elif (time_hours_int == 12):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 12.txt", "a")
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

            elif (time_hours_int == 13):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 13.txt", "a")
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

            elif (time_hours_int == 14):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 14.txt", "a")
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

            elif (time_hours_int == 15):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 15.txt", "a")
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

            elif (time_hours_int == 16):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 16.txt", "a")
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

            elif (time_hours_int == 17):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 17.txt", "a")
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

            elif (time_hours_int == 18):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 18.txt", "a")
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

            elif (time_hours_int == 19):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 19.txt", "a")
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

            elif (time_hours_int == 20):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 20.txt", "a")
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

            elif (time_hours_int == 21):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 21.txt", "a")
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

            elif (time_hours_int == 22):
                print("yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 22.txt", "a")
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

            elif (end_time_hours == 23):
                print("Yes")
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
                            time.sleep(15)
                            response = session.get(RequestUrl)
                            response = session.get(RequestUrl) #Update called after the delay as the final set value to be stored in the file
                            RequestUrl_1 = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
                            response = session.get(RequestUrl_1)
                            r = session.put(RequestUrl_1)
                            res = json.loads(response.text)
                            new_level = res['data']['metrics']['level'] #Gets the new light level value after the delay; gives time for adjusting light level
                            light_data = open("Light Data 23.txt", "a")
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
                
            #print("Less than 7 days")
            updated_time = datetime.datetime.now() 
            updated_time_days = updated_time.strftime("%d")
            updated_time_days_int = int(updated_time_days)
            print(updated_time_days_int)
            
            updated_time_hours = updated_time.strftime("%H")
            time_hours_int = int(time_hours)
            print("Less than 7 days")
            time.sleep(1)
