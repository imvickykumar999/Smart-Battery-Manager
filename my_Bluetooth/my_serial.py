
import serial
Arduino_Serial = serial.Serial('com8', 9600)

input_data = input().encode()
Arduino_Serial.write(input_data)
# Arduino_Serial.write(b'0')