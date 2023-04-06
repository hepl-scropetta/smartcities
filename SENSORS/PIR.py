# Code copier sur https://bhave.sh/micropython-detect-motion/

from machine import Pin
from time import sleep

motion_pin = Pin(20, Pin.IN)
led_pin = Pin(25, Pin.OUT)

ON_TIME = 10
SLEEP_TIME = 0.5
countdown = 0

while True:
    if motion_pin.value():
        led_pin.on()
        countdown = ON_TIME
    
    sleep(SLEEP_TIME)
    countdown = countdown - SLEEP_TIME

    if countdown <= 0:
        led_pin.off()