import os
import network
import ntptime
import utime
from machine import Pin
from umqtt.simple import MQTTClient
from dht import DHT11
from lcd1602 import LCD1602
from machine import *

REFRESH_INTERVAL = 1000
DHT_INTERVAL = 5000 #number of microsecond before LCD refresh
last_refresh_time = 0
last_dht_time = 0

last_refresh_datetime = 0

rtc = RTC()
dht11 = DHT11(Pin(18))
luminosite_adc = ADC(1)
i2c_1 = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c_1, 2, 16)
d.display()
d.clear()

percentChar = [
  0b00000,
  0b11001,
  0b11010,
  0b00010,
  0b00100,
  0b01000,
  0b01011,
  0b10011
]

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

d.create_char(0,percentChar)
d.create_char(1,degreChar)

# Create a header row for the CSV file
header = "Timestamp,Temperature\n"
filename = "temperatures.csv"

# Create new file if it doesn't exist
if filename not in os.listdir():
    with open(filename, 'w') as f:
        f.write(header)

# Network setup
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# wlan.connect("electroProjectWifi", "M13#MRSE")
wlan.connect("WiFi-2.4-B4E5","185E23AC26")
while not wlan.isconnected():
    pass  

print("WLAN ok")

def saveData(temp, hum, lum):
    timestamp = utime.localtime()
    # Format the timestamp and temperature as strings
    timestamp_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(*timestamp)
    temperature_str = "{}".format(temp)
    humidity_str = "{}".format(hum)
    luminosity_str = "{}".format(lum)

    # Write the timestamp and temperature to the CSV file
    line = "{},{},{},{}\n".format(timestamp_str, temperature_str, humidity_str, luminosity_str)
    try:
        print(timestamp_str)
        print(wlan.isconnected())
        serveur.publish("TristanScropetta",line)
    except:
        print("Can't publish")

    f.write(line)

def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def callBackMQTT_msg(topic, msg):
    global alarme_status 
    global topic_status
    alarme_status = msg
    topic_status = topic
    print(f"Message received: {topic.decode()}: {msg.decode()}")

serveur = MQTTClient(client_id="picow", 
                    server=b"c0deea5d7e584e5fadc9488cba7cb0bf.s2.eu.hivemq.cloud", 
                    port=8883, 
                    user= "picow", 
                    password="Azertyuiop1",
                    keepalive=60,
                    ssl=True,
                    ssl_params={'server_hostname':'c0deea5d7e584e5fadc9488cba7cb0bf.s2.eu.hivemq.cloud'}
)
serveur.connect()
serveur.set_callback(callBackMQTT_msg)
serveur.subscribe("TristanScropetta/temp")

ntptime.settime()
rtc = RTC()
utc_shift = 2

tm = utime.localtime(utime.mktime(utime.localtime()) + utc_shift*3600)
print(tm)
tm = tm[0:3] + (0,) + tm[3:6] + (0,)
print(tm)
rtc.datetime(tm)
print("RTC OK")
_datetime = rtc.datetime()
# Open the CSV file in write mode
with open(filename, "a") as f:

    while True:
        if utime.ticks_ms() - last_refresh_time >= REFRESH_INTERVAL:
            last_refresh_time = utime.ticks_ms()
            _datetime = rtc.datetime()
            saveData(dht11.temperature(), dht11.humidity(), str(map_range(luminosite_adc.read_u16(),0, 40000,0,100)) )

        d.setCursor(0, 0)
        d.print("{}:{}:{} {}/{}/{}".format(_datetime[4],_datetime[5],_datetime[6],_datetime[2],_datetime[1],_datetime[0]))

        if utime.ticks_ms() - last_dht_time >= DHT_INTERVAL:
            try:
                last_dht_time = utime.ticks_ms()
                dht11.measure()
                d.clear()
                d.setCursor(0, 1)
                d.print(str(dht11.temperature()))
                # serveur.publish("TristanScropetta/temp",str(dht11.temperature()))
                d.print(chr(1) + " ")
                d.print(str(dht11.humidity()))
                # serveur.publish("TristanScropetta/hum",str(dht11.humidity()))
                d.print(chr(0) + " ")
                d.print(str(map_range(luminosite_adc.read_u16(),0, 40000,0,100)))
                # serveur.publish("TristanScropetta/lum",str(map_range(luminosite_adc.read_u16(),0, 40000,0,100)))
                d.print(chr(0))
            except:
                print("Error")