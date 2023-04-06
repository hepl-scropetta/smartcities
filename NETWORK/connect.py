import network
import ntptime
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('electroProjectWifi', 'M13#MRSE')

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)

ntptime.settime()	# this queries the time from an NTP server
print(time.localtime())

print(wlan.ifconfig())
