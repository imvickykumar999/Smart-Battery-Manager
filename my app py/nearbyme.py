
import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_name = True)

for addr, name in nearby_devices:
    print("name = ", name)
    print("addr = ", addr)

