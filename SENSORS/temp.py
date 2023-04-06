from dht import DHT11
from machine import Pin, I2C
from utime import sleep

dht11 = DHT11(Pin(18))

while True:
    sleep(0.5)
    dht11.measure()
    print(dht11.temperature())
    print(dht11.humidity())