
import serial
Arduino_Serial = serial.Serial('com8', 9600)

while 1:
    input_data = input().encode()
    Arduino_Serial.write(input_data)
    # Arduino_Serial.write(b'0')