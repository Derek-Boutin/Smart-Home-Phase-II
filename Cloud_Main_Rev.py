import mysql.connector #Terminal: 'sudo apt-get install python3-mysql.connector'
import socket
import requests
import json
import threading
import numpy as np
from math import sqrt
from collections import Counter
import matplotlib.pyplot as plt
import time


def openDB():
    con = mysql.connector.connect(user='Smart_Home_user', password='laurensellers',
    host='127.0.0.1', database='Smart_Home_db')
    return con

def insertExtraRoomRSSI(RSSI_1, RSSI_2, RSSI_3):
    conn = openDB()
    cursor = conn.cursor()
    query = ("INSERT INTO extra_room (ID, RSSI_1, RSSI_2, RSSI_3) VALUES (NULL, %s, %s, %s)")
    query1 = (RSSI_1, RSSI_2, RSSI_3)
    cursor.execute(query, query1)
    conn.commit()
    cursor.close()
    conn.close()

def insertBedRoomRSSI(RSSI_1, RSSI_2, RSSI_3):
    conn = openDB()
    cursor = conn.cursor()
    query = ("INSERT INTO bed_room (ID, RSSI_1, RSSI_2, RSSI_3) VALUES (NULL, %s, %s, %s)")
    query1 = (RSSI_1, RSSI_2, RSSI_3)
    cursor.execute(query, query1)
    conn.commit()
    cursor.close()
    conn.close()

def insertMachineLearningExtraRoom(old_light, new_level):
    conn = openDB()
    cursor = conn.cursor()
    query = ("INSERT INTO light_learning_extra_room(ID, lux, percent) VALUES (NULL, %s, %s)")
    query1 = (old_light, new_level)
    cursor.execute(query, query1)
    conn.commit()
    cursor.close()
    conn.close()

def insertMachineLearningBedRoom(old_light, new_level):
    conn = openDB()
    cursor = conn.cursor()
    query = ("INSERT INTO light_learning_bed_room(ID, x_value, y_value) VALUES (NULL, %s, %s)")
    query1 = (old_light, new_level)
    cursor.execute(query, query1)
    conn.commit()
    cursor.close()
    conn.close()

def insertMachineLearningLivingRoom(old_light, new_level):
    conn = openDB()
    cursor = conn.cursor()
    query = ("INSERT INTO light_learning_living_room(ID, lux, percent) VALUES (NULL, %s, %s)")
    query1 = (old_light, new_level)
    cursor.execute(query, query1)
    conn.commit()
    cursor.close()
    conn.close()

def insertMachineLearningLivingRoom(old_light, new_level):
    conn = openDB()
    cursor = conn.cursor()
    query = ("INSERT INTO light_learning_living_room(ID, x_value, y_value) VALUES (NULL, %s, %s)")
    query1 = (old_light, new_level)
    cursor.execute(query, query1)
    conn.commit()
    cursor.close()
    conn.close()

def insertLivingRoomRSSI(RSSI_1, RSSI_2, RSSI_3):
    conn = openDB()
    cursor = conn.cursor()
    query = ("INSERT INTO living_room (ID, RSSI_1, RSSI_2, RSSI_3) VALUES (NULL, %s, %s, %s)")
    query1 = (RSSI_1, RSSI_2, RSSI_3)
    cursor.execute(query, query1)
    conn.commit()
    cursor.close()
    conn.close()

def getExtraRoom():
    conn = openDB()
    cursor = conn.cursor()
    query = ("SELECT RSSI_1, RSSI_2, RSSI_3 FROM extra_room")
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    if (data == None):
        return None
    return data

def getBedRoom():
    conn = openDB()
    cursor = conn.cursor()
    query = ("SELECT RSSI_1, RSSI_2, RSSI_3 FROM bed_room")
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    if (data == None):
        return None
    return data

def getLivingRoom():
    conn = openDB()
    cursor = conn.cursor()
    query = ("SELECT RSSI_1, RSSI_2, RSSI_3 FROM living_room")
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    if (data == None):
        return None
    return data


def Least_Squares(room):
    conn = openDB()
    cursor = conn.cursor()
    x_coords, y_coords = [],[]
    # execute the SQL query using execute() method.
    if (room == 'extra-room'):
        query = "SELECT lux, percent from light_learning_extra_room"
        cursor.execute(query)
        # fetch all of the rows from the query
        data = cursor.fetchall()
        # print the rows
        for row in data:
            x_coords.append(row[0])
            y_coords.append(row[1])
            
        cursor.close()
        conn.close()
        x = np.array(x_coords)
        y = np.array(y_coords)
        new_y = 100-y
        '''
        This is to account for the positive slope that results from using the algorithm;
        need to change this back when ready for the final values
        '''
        b = estimate_coef(x, new_y)
        #print("Estimated Coeficients:\nm = {} \ \ny-int= {}".format(b[1], b[0]))
        m=b[1]
        y_int = b[0]
        #plotting regression line
        plot_regression_line(x, new_y,b)
        return m,y_int
    else:
        m=0
        y_int=0
        return m,y_int
   
def light_poller(name, light, room, output_level):
    global old_room
    time.sleep(30)
    topLevelUrl = 'http://192.168.1.23:8083'
    LoginUrl = topLevelUrl + '/ZAutomation/api/v1/login'

    username = 'admin'
    password = 'laurensellers'

    LoginHeader = {'User-Agent': 'Mozilla/5.0', 'Cotent-Type': 'application/json'}
    Formlogin = '{"form": true, "login": "'+username+'", "password": "'+password+'", "keepme": false, "default_ui": 1}'

    session = requests.Session()
    session.post(LoginUrl, headers=LoginHeader, data=Formlogin)
    
    RequestUrl_Update = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/update' #Updates light level from dashboard
    response = session.get(RequestUrl_Update)
    response = session.get(RequestUrl_Update) #Called a second time to send it back to be outputted in the shell
    RequestUrl_Poll = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38'
    response = session.get(RequestUrl_Poll)
    res = json.loads(response.text)
    new_level = res['data']['metrics']['level']
    print("New Switch level Poller " + str(new_level))
    if (old_room == room):
        #update db for light
        print("Updated")
        if (room == 'extra-room'):
            insertMachineLearningExtraRoom(light, new_level)
        '''
        elif (room == 'bedroom'):
            insertMachineLearningBedRoom(light, new_level)

        elif (room == 'living-room'):
            insertMachineLearningLivingRoom(light, new_level)
        '''  
        

def phone_listener():
    port = 5000 # port number
    host = '192.168.1.30' #ip address of cloud
    dataset = createDataSet()
    k = 3
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket
    s.bind((host, port))
    s.listen(5) #listen for max 5 connections
    #print("Hub listening....")
    #print("Cloud Listening...")
    while True:
        client, address = s.accept()
        address = str(address)
        print("Connecting with " + str(address))
        phone_lightlevel = client.recv(1024).decode('UTF-8')
        topLevelUrl = 'http://192.168.1.23:8083'
        LoginUrl = topLevelUrl + '/ZAutomation/api/v1/login'
        username = 'admin'
        password = 'laurensellers'
        LoginHeader = {'User-Agent': 'Mozilla/5.0', 'Cotent-Type': 'application/json'}
        Formlogin = '{"form": true, "login": "'+username+'", "password": "'+password+'", "keepme": false, "default_ui": 1}'
        session = requests.Session()
        session.post(LoginUrl, headers=LoginHeader, data=Formlogin)
        RequestUrl = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/exact?level=' + phone_lightlevel
        response = session.get(RequestUrl)


def createDataSet():
    data = getExtraRoom()
    extra_room_list = []
    bed_room_list = []
    living_room_list = []
    for n in data:
        extra_room_list.append(n)
    data = getBedRoom()
    for n in data:
        bed_room_list.append(n)
    data = getLivingRoom()
    for n in data:
        living_room_list.append(n)
    dataset = {'extra-room': extra_room_list, 'bedroom': bed_room_list, 'living-room': living_room_list}
    return dataset

def k_nearest_neighbor(data, predict, k):
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])
    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result

def estimate_coef(x, y):
    # number of observations/points
    print(x,y)
    n = np.size(x)
    print(n)
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
    print(m_x,m_y)
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x - n*m_y*m_x)
    SS_xx = np.sum(x*x - n*m_x*m_x)
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    return(b_0, b_1)

def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
    # predicted response vector
    y_pred = b[0] + b[1]*x
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
      # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
    # function to show plot
    plt.show()
        
def Do_Math(name, client, dataset, k):
    global old_room
    global initial
    jsonReceived = client.recv(1024).decode('UTF-8')
    dataRecevied = json.loads(jsonReceived)
    RSSI_data =[]
    for data in dataRecevied:
        RSSI_data.append(data['RSSI'])
    print(dataRecevied)
    #print(dataset)
    light_level = dataRecevied[0]
    #should be the light level parsed from received data of ID 1
    light = light_level['light_level']
    float_light = float(light)
    int_light = int(float_light)
    RSSI_array = list(map(int, RSSI_data))
    RSSI_1 = RSSI_array[0]
    RSSI_2 = RSSI_array[1]
    RSSI_3 = RSSI_array[2]
    
    #For Localization Machine Learning; comment this block when finished with training
    #insertExtraRoomRSSI(RSSI_1, RSSI_2, RSSI_3)
    #insertLivingRoomRSSI(RSSI_1, RSSI_2, RSSI_3)
    #insertBedRoomRSSI(RSSI_1, RSSI_2, RSSI_3)

    #For k-NN Algorithm:
    room_prediction = k_nearest_neighbor(dataset, RSSI_array, k)
    print("Prediction " + room_prediction)
    
    #Polling Light Level for Least Squares database
    print("Old " + old_room)
    if (old_room != room_prediction):
        if (room_prediction == 'extra-room'):
            m,y_int = Least_Squares(room_prediction)
            output = int_light*(m) + (y_int)
            output = int(output)
            output_level = 100 - output
            str_output_level= str(output_level)
            print("output: " + str_output_level)
            #send to hub to adjust light level
            j = json.dumps(str_output_level)
            client.sendall(j.encode('utf-8'))
            client.close()
            poller = threading.Thread(target=light_poller, args=("Poller", int_light, room_prediction, output_level))
            poller.start()
        if (old_room == 'extra-room' and initial == False):
            print("Should be off")
            topLevelUrl = 'http://192.168.1.23:8083'
            LoginUrl = topLevelUrl + '/ZAutomation/api/v1/login'
            username = 'admin'
            password = 'laurensellers'
            LoginHeader = {'User-Agent': 'Mozilla/5.0', 'Cotent-Type': 'application/json'}
            Formlogin = '{"form": true, "login": "'+username+'", "password": "'+password+'", "keepme": false, "default_ui": 1}'
            session = requests.Session()
            session.post(LoginUrl, headers=LoginHeader, data=Formlogin)
            RequestUrl_Poll = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/off'
            response = session.get(RequestUrl_Poll)
            print(response)
    
    old_room = room_prediction
    initial = False
    print("New " + old_room)

    
def hub_conn():
    port = 6000 # port number
    old_room = ''
    host = '192.168.1.30' #ip address of cloud
    dataset = createDataSet()
    k = 3
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket
    s.bind((host, port))
    topLevelUrl = 'http://192.168.1.23:8083'
    LoginUrl = topLevelUrl + '/ZAutomation/api/v1/login'
    username = 'admin'
    password = 'laurensellers'
    LoginHeader = {'User-Agent': 'Mozilla/5.0', 'Cotent-Type': 'application/json'}
    Formlogin = '{"form": true, "login": "'+username+'", "password": "'+password+'", "keepme": false, "default_ui": 1}'
    session = requests.Session()
    session.post(LoginUrl, headers=LoginHeader, data=Formlogin)
    RequestUrl_Off = topLevelUrl + '/ZAutomation/api/v1/devices/ZWayVDev_zway_10-0-38/command/off' #Updates light level from dashboard
    response = session.get(RequestUrl_Off)
    s.listen(5) #listen for max 5 connections
    #print(threading.active_count())
    print("Cloud Listening...")
    
    while True:
        client, address = s.accept()
        address = str(address)
        print("Connecting with " + str(address))
        run = threading.Thread(target=Do_Math, args=("Connection", client, dataset, k))
        run.start()
        #client.send(output.encode('utf-8'))
        #client.close()
        
def main():
    k = 3
    old_light = 0
    old_level = 0
    initial = True
    old_room = ''
    i = 0
    x_coords = []
    y_coords = []
    conn = threading.Thread(target=hub_conn)
    conn.start()
    phone_listener()
    
main()