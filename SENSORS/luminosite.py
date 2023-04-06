import machine

luminosite_adc = machine.ADC(1)

while True:
    # Lecture de la tension de luminosité
    lum = luminosite_adc.read_u16()

    # Affichage de la luminosité
    print(lum)
