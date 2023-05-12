import network
from machine import Pin
from umqtt.simple import MQTTClient
from neopixel import NeoPixel
import utime

np = NeoPixel(Pin(18), 30)
motion = Pin(20, Pin.IN)
alarme_status = b''
topic_status = b''
detectTime = 0
motionIsActive = False
motionWasActive = True
alarmeIsActive = False

def callBackMQTT_msg(topic, msg):
    global alarme_status 
    global topic_status
    alarme_status = msg
    topic_status = topic
    print(f"Message received: {topic.decode()}: {msg.decode()}")

def toggleAlarme(isActive):
    if(isActive):
        np.fill((255,255,255))
        for j in range(10,20):
            np.__setitem__(j, (255,0,0))
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
wlan.connect("electroProjectWifi", "M13#MRSE")
# wlan.connect("WiFi-2.4-B4E5","185E23AC26")
while not wlan.isconnected():
    pass  

print("WLAN ok")

serveur = MQTTClient(client_id="picow", 
                    server=b"c0deea5d7e584e5fadc9488cba7cb0bf.s2.eu.hivemq.cloud", 
                    port=8883, 
                    user= "picow", 
                    password="Azertyuiop1",
                    keepalive=7200,
                    ssl=True,
                    ssl_params={'server_hostname':'c0deea5d7e584e5fadc9488cba7cb0bf.s2.eu.hivemq.cloud'}
)

serveur.connect()
serveur.set_callback(callBackMQTT_msg)
serveur.subscribe("alarme")
serveur.subscribe("temp")
print("setup ready")
toggleLight(False)

while True:
    if motion.value():
        motionIsActive = True
        detectTime = utime.time()
        toggleLight(True)

        if motionWasActive == True:
            motionWasActive = False
            serveur.publish("movement","ON")

    if utime.time() - detectTime > 5 & detectTime != 0 :
        motionIsActive = False
        motionWasActive = True
        serveur.publish("movement","OFF")
        toggleLight(False)
        detectTime = 0

    serveur.check_msg()
    if topic_status != b'':
        print("notify")
        if topic_status.decode() == "alarme":
            topic_status = b''
            status = alarme_status.decode()
            if status == "ON":
                print("alarme ON")
                alarmeIsActive = True
                toggleAlarme(True)
                continue
            if status == "OFF":
                print("alarme OFF")
                alarmeIsActive = False
                toggleAlarme(False)
                continue
            else:
                print("ERROR ALARM CMD")
        
    if alarmeIsActive:
        if utime.time() % 2:
            toggleAlarme(True)
        else:
            toggleAlarme(False)
