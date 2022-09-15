    
import psutil, time, serial
Arduino_Serial = serial.Serial('com8', 9600)

i = 0
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

# maxbat = 97
# minbat = 30
# print(percent)

maxbat = percent+1
minbat = percent-1

if plugged == False:
    plugged = "Not Plugged In"
else:
    plugged = "Plugged In"

status = str(percent) + '% | ' + plugged
print(status)

count = 0
data = []
while True:

    battery = psutil.sensors_battery()
    pluggedbool = battery.power_plugged
    percent = battery.percent
    
    if pluggedbool == False:
        plugged = "Not Plugged In"
    else:
        plugged = "Plugged In"
        
    count += 1
    i += 1
    data.append(percent)

    print(str(count), '). ', str(percent), '[', str(maxbat), str(minbat), ']', plugged, str(battery))
    time.sleep(3)

    if percent >= maxbat:
        text = '0000000000000000000'
        input_data = text.encode()
        Arduino_Serial.write(input_data)

        # print("\nWaiting for 60 seconds...\n")
        # time.sleep(60)
        continue

    if percent <= minbat:
        text = '11111111111111111111'
        input_data = text.encode()
        Arduino_Serial.write(input_data)

        # print("\nWaiting for 60 seconds...\n")
        # time.sleep(60)
        continue

    else:
        continue
