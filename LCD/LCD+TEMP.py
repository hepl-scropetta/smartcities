from lcd1602 import LCD1602
from dht import DHT11
from machine import I2C,Pin,ADC,PWM
from utime import sleep

dht11 = DHT11(Pin(18))
i2c_1 = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
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

while True:
    sleep(0.5)
    dht11.measure()
    d.clear()
    d.setCursor(0, 0)
    d.print(str(dht11.temperature()))
    d.print(chr(1))
    d.setCursor(0, 1)
    d.print(str(dht11.humidity()))
    d.print(chr(0))
    sleep(0.5)