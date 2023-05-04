import network
from umqtt.simple import MQTTClient

def callBackMQTT_msg(topic, msg):
    print(f"Message received: {topic}: {msg}")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("electroProjectWifi", "M13#MRSE")
while not wlan.isconnected():
    pass  

print("WLAN ok")

serveur = MQTTClient("pi", "192.168.2.131", port=1883)
serveur.connect()
serveur.set_callback(callBackMQTT_msg)
serveur.subscribe("test")

while True:
    serveur.check_msg()