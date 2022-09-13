# Laptop-Auto-Charger-using-Arduino-and-Relay

- [See Project Video](https://github.com/imvickykumar999/Laptop-Auto-Charger-using-Arduino-and-Relay/blob/main/final%20project/WhatsApp%20Video%202022-09-09%20at%2000.53.42.mp4)
- [.exe file for Windows](https://github.com/imvickykumar999/Laptop-Auto-Charger-using-Arduino-and-Relay/blob/main/final%20project/autosocket.exe)
- [.apk file for Android](https://github.com/imvickykumar999/Laptop-Auto-Charger-using-Arduino-and-Relay/blob/main/final%20project/battery.apk)

-----------------------

`Bulb has been replaced with Charger`
![charger](https://user-images.githubusercontent.com/50515418/174425972-de004c74-49f4-4e75-96c2-61e6e4609cef.png)

------------------------------

# Upload into Arduino : [my_bluetooth.ino](https://github.com/imvickykumar999/Laptop-Auto-Charger-using-Arduino-and-Relay/blob/main/my_Bluetooth/my_Bluetooth.ino)

        char inputByte;

        void setup() {
         Serial.begin(9600);
         pinMode(13,OUTPUT);
         digitalWrite(13,HIGH);
        }

        void loop() {
          while(Serial.available()>0){

              inputByte = Serial.read();
              Serial.println(inputByte);

              if (inputByte=='1'){
              digitalWrite(13,HIGH);
            }

            else if (inputByte=='0'){
              digitalWrite(13,LOW);
              } 
            }
        }

------------------------------------

# Publishing on Play Store

[![ss](https://github.com/imvickykumar999/Laptop-Auto-Charger-using-Arduino-and-Relay/blob/main/Screenshot_20220913-231746.jpg?raw=true)](https://www.youtube.com/watch?v=5GHT4QtotE4)
