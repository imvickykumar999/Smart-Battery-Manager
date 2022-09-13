
# https://people.csail.mit.edu/albert/bluez-intro/c212.html

import bluetooth

target_name = "Vicky Kumar"
target_address = 'FC:A8:9A:00:21:16'

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print ("found target bluetooth device with address ", target_address)
else:
    print ("could not find target bluetooth device nearby")
