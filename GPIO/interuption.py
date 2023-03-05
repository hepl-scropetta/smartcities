# Scropetta Tristan
# 05/03/2023
# Ce code est réalisé dans le cadre d'un cours de l'HEPL

from machine import Pin # On import la class Pin qui permet de représenter une Pin "réel"

push = Pin(18, Pin.IN) # Définition de l'objet push sur la pin 18
led = Pin(20, Pin.OUT) # Définition de l'objet led sur la pin 20

def toggle_led(p):		# Création d'une fonction qui sera le handler de notre iteruption
    led.toggle()		# Fonction toggle de la class Pin qui permet d'inverser l'étét d'une sortie "Pin"
    
push.irq(toggle_led,trigger=Pin.IRQ_RISING)	#Déclaration de notre iteruption. 1er argument le handler, notre fonction toggle_led();
                                            #l'argument trigger défini le type de déclanchement, ici on choisi sur le flanc montant

while True:		# Une boucle infinie pour que le programme continue de tourner, sinon l'interuption ne peut fonctionner.
    pass
