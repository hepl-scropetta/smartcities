from machine import Pin, I2C, ADC, PWM
from time import sleep

blanche = 2
noire = 1
croche = 0.5
doublecroche = 0.25

buzzer = PWM(Pin(20))
vol = 1000

%Gamme 4
def DO_1(time):
    buzzer.freq(523) #1
    buzzer.duty_u16(vol)
    sleep(time)
def RE_1(time):    
    buzzer.freq(587) #2
    buzzer.duty_u16(vol)
    sleep(time)
def RE_d_1(time):
    buzzer.freq(622) #2
    buzzer.duty_u16(vol)
    sleep(time)
def MI_1(time):          
    buzzer.freq(659) #3
    buzzer.duty_u16(vol)
    sleep(time)
def FA_1(time):     
    buzzer.freq(698) #4
    buzzer.duty_u16(vol)
    sleep(time)
def SO_1(time):    
    buzzer.freq(784) #5
    buzzer.duty_u16(vol)
    sleep(time)
def LA_1(time):    
    buzzer.freq(880) #6
    buzzer.duty_u16(vol)
    sleep(time)
def SI_1(time):
    buzzer.freq(988) #1
    buzzer.duty_u16(vol)
    sleep(time)
    
% Gamme 5
def DO(time):
    buzzer.freq(1046) #1
    buzzer.duty_u16(vol)
    sleep(time)
def RE(time):    
    buzzer.freq(1175) #2
    buzzer.duty_u16(vol)
    sleep(time)
def RE_d(time):
    buzzer.freq(1244) #2
    buzzer.duty_u16(vol)
    sleep(time)
def MI(time):          
    buzzer.freq(1318) #3
    buzzer.duty_u16(vol)
    sleep(time)
def FA(time):     
    buzzer.freq(1397) #4
    buzzer.duty_u16(vol)
    sleep(time)
def SO(time):    
    buzzer.freq(1568) #5
    buzzer.duty_u16(vol)
    sleep(time)
def LA(time):    
    buzzer.freq(1760) #6
    buzzer.duty_u16(vol)
    sleep(time)
def SI(time):    
    buzzer.freq(1967) #7
    buzzer.duty_u16(vol)
    sleep(time)
def N(time):
    buzzer.duty_u16(0) #close
    sleep(time)
    
MI(doublecroche)
RE_d(doublecroche)
MI(doublecroche)
RE_d(doublecroche)
MI(doublecroche)

SI_1(doublecroche)
RE(doublecroche)
DO(doublecroche)
LA_1(noire)

DO_1(doublecroche)
MI_1(doublecroche)
LA_1(doublecroche)
SI(noire)

N(1)
