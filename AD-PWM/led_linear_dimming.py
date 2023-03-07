from machine import Pin
import utime

pwm = PWM(Pin(20))
pwm.freq(500)

while True:
    for i in range(20):
        pwm.duty_u16(i*3276)
        utime.sleep_ms(100)