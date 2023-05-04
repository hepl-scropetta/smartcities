import umqtt.simple
import network
from utime import sleep

    
# 0   STAT_IDLE -- no connection and no activity,
# 1   STAT_CONNECTING -- connecting in progress,
# -3  STAT_WRONG_PASSWORD -- failed due to incorrect password,
# -2  STAT_NO_AP_FOUND -- failed because no access point replied,
# -1  STAT_CONNECT_FAIL -- failed due to other problems,
# 3   STAT_GOT_IP -- connection successful.

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("electroProjectWifi", "M13#MRSE")
while not wlan.isconnected():
    print(wlan.status())
    pass   
    
print("WLAN ok.")
sleep(5)

serveur = umqtt.simple.MQTTClient("p", "192.168.2.131" ,port=1883)
serveur.connect()
serveur.publish("test","Hello de mon Pico 2W!")
