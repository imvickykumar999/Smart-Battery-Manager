    
import psutil, time, serial

battery = psutil.sensors_battery()
percent = battery.percent

com = 'com8'
maxbat = percent+1
minbat = percent-1

# maxbat = 97
# minbat = 30
Arduino_Serial = serial.Serial(com, 9600)

count = i = 0
data = []
while True:

    battery = psutil.sensors_battery()
    percent = battery.percent

    count += 1
    i += 1
    data.append(percent)

    print(str(percent), '[', str(maxbat), ',',  str(minbat), ']', battery[2])
    time.sleep(3)

    if percent >= maxbat:
        text = '0'
        input_data = text.encode()
        Arduino_Serial.write(input_data)

    if percent <= minbat:
        text = '1'
        input_data = text.encode()
        Arduino_Serial.write(input_data)

    continue
