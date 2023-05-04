import network
import urequests
import ntptime
import time
import utime
from machine import I2C, Pin    
from lcd1602 import LCD1602

i2c_1 = I2C(1, scl=Pin(7), sda=Pin(6))
dis = LCD1602(i2c_1, 2, 16)
dis.display()
dis.clear()

degreChar = [
	0b00111,
	0b00101,
	0b00111,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00000
]

dis.create_char(0,degreChar)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Proximus-Home-FDF0', 'wzmjcra6xhaea')

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)

print(wlan.ifconfig())

ntptime.settime()	# this queries the time from an NTP server

key = {'lat': '50.8081',
       'lon': '4.3874',
       'appid': '683e45bf0e0fb0e8b3958acd57b401e3',
       'units': 'metric'}

url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + key['lat'] + '&lon=' + key['lon'] + '&appid=' + key['appid'] +'&units=' + key['units']
print(url)

while True:
    _time = time.localtime()
    hours = _time[3] + 2
    min = _time[4]
    sec = _time[5]
    if sec == 0:
        dis.clear()
        r = urequests.get(url)
        j = r.json()
        dis.setCursor(0,1)
        dis.print(str(j["main"]["temp"]))
        dis.print(chr(0))
        dis.print("C " + str(j["main"]["humidity"]) + " %")
    print("{} : {} : {}".format(hours, min, sec))
    dis.setCursor(0,0)
    dis.print(str(hours))
    dis.print(":")
    dis.print(str(min))
    dis.print(":")
    dis.print(str(sec))
    dis.setCursor(11, 0)
    dis.print("{}/{}".format(_time[2], _time[1]))
    dis.display()

