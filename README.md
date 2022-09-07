## Laptop-Auto-Charger-using-Arduino-and-Relay

`Bulb has been replaced with Charger`
![charger](https://user-images.githubusercontent.com/50515418/174425972-de004c74-49f4-4e75-96c2-61e6e4609cef.png)

------------------------------

## my_bluetooth.ino

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

