import machine
import time

# Configuration du port GPIO 26 en entrée analogique
mic = machine.ADC(26)

while True:
    # Lecture de la valeur analogique
    audio_level = mic.read_u16()
    print(audio_level)
    time.sleep(0.1)
