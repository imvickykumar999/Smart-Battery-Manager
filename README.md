# Laptop-Auto-Charger-using-Arduino-and-Relay

---------------------------

- [See Project Video](https://github.com/imvickykumar999/Laptop-Auto-Charger-using-Arduino-and-Relay/blob/main/final%20project/WhatsApp%20Video%202022-09-09%20at%2000.53.42.mp4)
- [.exe file for Windows](https://github.com/imvickykumar999/Laptop-Auto-Charger-using-Arduino-and-Relay/blob/main/final%20project/autosocket.exe)
- [.apk file for Android](https://github.com/imvickykumar999/Laptop-Auto-Charger-using-Arduino-and-Relay/blob/main/final%20project/battery.apk)

--------------------------------------

[![final block code mit](https://github.com/imvickykumar999/Smart-Battery-Manager/blob/main/final%20project/blocks%20(2).png?raw=true)](https://github.com/imvickykumar999/Smart-Battery-Manager/blob/main/final%20project/GoogleAccount_checkpoint1.apk)

------------------------------------

# Publishing on Play Store : [YouTube Tutorial](https://www.youtube.com/watch?v=5GHT4QtotE4)

<table>
   <tr>
      <td><img src="https://github.com/imvickykumar999/Smart-Battery-Manager/blob/main/android%20apk/relay%20bluetooth/WhatsApp%20Image%202022-09-19%20at%2000.05.33.jpeg?raw=true?raw=true" alt="3" width = 400px></td>
      <td><img src="https://github.com/imvickykumar999/Laptop-Auto-Charger-using-Arduino-and-Relay/blob/main/Screenshot_20220913-231746.jpg?raw=true" align="right" alt="4" width = 400px></td>
  </tr>
</table>

-----------------------

# `Bulb` has been replaced with `Charger`

![charger](https://user-images.githubusercontent.com/50515418/174425972-de004c74-49f4-4e75-96c2-61e6e4609cef.png)

--------------------------------

# `4 Channel Relay` Circuit Diagram : [Firebase Login](https://console.firebase.google.com/u/0/project/home-automation-336c0/database/home-automation-336c0-default-rtdb/data/~2FA~2FB~2FC~2FSwitch)

![image](https://user-images.githubusercontent.com/50515418/190896691-56ffb755-f804-4aab-909b-736becf829a3.png)

------------------------------

## `Wi-Fi Mode`

    #include <WiFi.h>
    #include "FirebaseESP32.h"
    //#include <Servo.h>
    int servoPin = 2; // D2 PIN
    //Servo Servo1;
    #define WIFI_SSID "Vicky"
    #define WIFI_PASSWORD "*********"
    #define FIREBASE_HOST "home-automation-336c0-default-rtdb.firebaseio.com"
    #define FIREBASE_AUTH "********************************"
    FirebaseData firebaseData;
    void setup() {
    //  Servo1.attach(servoPin);
      Serial.begin(115200);
      WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
      Serial.print("Connecting to Wi-Fi");
      while (WiFi.status() != WL_CONNECTED)
      {
        Serial.print(".");
        delay(300);
      }
      Serial.println();
      Serial.print("Connected with IP: ");
      Serial.println(WiFi.localIP());
      Serial.println();
      Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
      Firebase.reconnectWiFi(true);
      //Set database read timeout to 1 minute (max 15 minutes)
      Firebase.setReadTimeout(firebaseData, 1000 * 60);
      pinMode(servoPin, OUTPUT);
    }
    void loop() {
        if (Firebase.getInt(firebaseData,"/A/B/C/Switch"))
        {
          int val2 = (firebaseData.intData());

          if(val2==1){
            digitalWrite(servoPin, HIGH);
            Serial.println("HIGH");
          }

          else{
            digitalWrite(servoPin, LOW);
            Serial.println("LOW");
          }
        }
        delay(200);
      // put your main code here, to run repeatedly:
    }

---------------------------------------

## `Bluetooth Mode`

    #include <SoftwareSerial.h>

    // use 10, 11 pair in Arduino Mega
    SoftwareSerial mySerial(8, 7); // RX, TX 
    char inputByte;

    void setup() {
     mySerial.begin(9600);
     Serial.begin(9600);
     Serial.println("Hello, world !");

     pinMode(13,OUTPUT);
     digitalWrite(13,HIGH);
    }

    void loop() {
      while(mySerial.available()>0){

          inputByte = mySerial.read();
    //      Serial.println(inputByte);

          if (inputByte=='1'){
          digitalWrite(13,HIGH);
        }

        else if (inputByte=='0'){
          digitalWrite(13,LOW);
          } 
        }
    }
