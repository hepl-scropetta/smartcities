import network
from machine import Pin
from umqtt.simple import MQTTClient
from neopixel import NeoPixel
import utime

np = NeoPixel(Pin(16), 8)
motion = Pin(20, Pin.IN)
alarme_status = b''
topic_status = b''
detectTime = 0

def callBackMQTT_msg(topic, msg):
    global alarme_status 
    global topic_status
    alarme_status = msg
    topic_status = topic
    print(f"Message received: {topic.decode()}: {msg.decode()}")

def toggleAlarme(isActive):
    if(isActive):
        np.fill((255,0,0))
    else:
        np.fill((255,255,255))
    np.write()

def toggleLight(isActive):
    if(isActive):
        np.fill((255,255,255))
    else:
        np.fill((25,25,25))
    np.write()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# wlan.connect("electroProjectWifi", "M13#MRSE")
wlan.connect("WiFi-2.4-B4E5","185E23AC26")
while not wlan.isconnected():
    pass  

print("WLAN ok")

serveur = MQTTClient("pi", "broker.hivemq.com", port=1883)
serveur.connect()
serveur.set_callback(callBackMQTT_msg)
serveur.subscribe("alarme")
serveur.subscribe("test")

while True:
    if motion.value():
        serveur.publish("movement","Motion Detected")
        detectTime = utime.time()
        toggleLight(True)

    if utime.time() - detectTime > 5 :
        toggleLight(False)
        detectTime = 0
        
    if serveur.check_msg() != None:
        if topic_status.decode() == "alarme":
            status = alarme_status.decode()
            if status == "ON":
                print("alarme ON")
                toggleAlarme(True)
                continue
            if status == "OFF":
                print("alarme OFF")
                toggleAlarme(False)
                continue
            else:
                print("ERROR ALARM CMD")
            