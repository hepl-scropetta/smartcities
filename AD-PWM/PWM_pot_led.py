from machine import Pin,ADC,PWM

ROTARY_ANGLE_SENSOR = ADC(0)
LED_PWM = pwm(Pin(18))

LED_PWM.freq(500)

while True:
    val = ROTARY_ANGLE_SENSOR.read_u16()
    print(val)
    LED_PWM.duty_u16(val)
    