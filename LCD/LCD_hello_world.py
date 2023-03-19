from lcd1602 import LCD1602
from machine import I2C,Pin
from utime import sleep
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16) 

d.display() 
d.blink()
sleep(1)
d.clear() 
d.print('Hello ') 

sleep(1)
d.setCursor(0, 1) 
d.print('world ')
d.no_blink()