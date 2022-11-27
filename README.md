# Laptop-Auto-Charger-using-Arduino-and-Relay

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
