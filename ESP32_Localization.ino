#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>
#include <WiFi.h>


int beaconScanTime = 1;

const char* ssid     = "NETGEAR31";
const char* password = "bluerabbit622";

const char* host = "192.168.1.27";
int port = 4000;

char rssiSend[20];
String rssi;
int INT_RSSI;
int status = WL_IDLE_STATUS;
WiFiClient client;

typedef struct {
  char address[17];   // MAC: d6:5e:c7:5f:2b:a6 
  int rssi;
} BeaconData;

uint8_t bufferIndex = 0;  // Found devices counter
BeaconData buffer[50];    // Buffer to store found device data
//int8_t message_char_buffer[MQTT_MAX_PACKET_SIZE];

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
public:

  void onResult(BLEAdvertisedDevice advertisedDevice) {
    extern uint8_t bufferIndex;
    extern BeaconData buffer[];
    if(bufferIndex >= 50) {
      return;
    }
    // RSSI
    if(advertisedDevice.haveRSSI()) {
      buffer[bufferIndex].rssi = advertisedDevice.getRSSI();
    } else { buffer[bufferIndex].rssi =  0; }
    
    // MAC is mandatory for BT to work
    strcpy (buffer[bufferIndex].address, advertisedDevice.getAddress().toString().c_str());
    
    bufferIndex++;
    //Serial.printf("name: %s \n", advertisedDevice.getName().c_str());
    
    
    String mac = advertisedDevice.getAddress().toString().c_str();
    if (mac == "d6:5e:c7:5f:2b:a6"){
      INT_RSSI = advertisedDevice.getRSSI();
    }
  }
  
    // Print everything via serial port for debugging
};

void setup() {
  Serial.begin(115200);
  BLEDevice::init(""); // Can only be called once
  // put your setup code here, to run once:

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    //delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  if (!client.connect(host, port)){
    Serial.println("Can't connect");
  }else{
    Serial.println("connected");
  }
}

void ScanBeacons() {
  
  BLEScan* pBLEScan = BLEDevice::getScan(); //create new scan
  MyAdvertisedDeviceCallbacks cb;
  pBLEScan->setAdvertisedDeviceCallbacks(&cb);
  pBLEScan->setActiveScan(true); //active scan uses more power, but get results faster
  BLEScanResults foundDevices = pBLEScan->start(beaconScanTime);
  
  //Serial.print(cb.getConcatedMessage());
 
  // Stop BLE
  pBLEScan->stop();
  
  Serial.println("Scan done!");
}

void loop() {
  Serial.println("Start Scan");
  boolean result;
  int total = 0;
  for (int i=0; i<3; i++){
    ScanBeacons();
    total = total + INT_RSSI;
  }
  int AVG_RSSI = total / 3;
  rssi = String(AVG_RSSI);
  Serial.println("Average RSSI: " + rssi);
  rssi = rssi + '0';
  rssi.toCharArray(rssiSend, rssi.length());
  
  ScanBeacons();

  bufferIndex = 0;
  
  if (!client.connected()){
      if (client.connect(host, port)){
        Serial.println("connected");
        Serial.println("Sending to Hub");
        client.write('4'); //ID of the device
        delay(10);
        Serial.println(rssiSend);
        client.write(rssiSend);
        rssiSend[0] = (char)0;
       // Serial.println("After" + rssiSend);
        client.stop();
      }else{
        Serial.println("could not connect");
        client.stop();
      }
    }else{
      Serial.println("not connected");
      client.stop();
      //delay(5000);
      return;
    }

  //delay(2000);
  // put your main code here, to run repeatedly:

}
