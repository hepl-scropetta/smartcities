from machine import Pin,PWM

from time import sleep

buzzer = PWM(Pin(20))
while True:
    buzzer.freq(1046)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1175)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1318)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1397)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1568)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1760)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1967)
    buzzer.duty_u16(1000)
    sleep(1)