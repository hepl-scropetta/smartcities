import machine 	# Permet d'importer tout les fonctions machine conçu pour les microcontrôler sous python

BUTTON = machine.Pin(16,machine.Pin.IN)	# Déclaration d'un object sur la pin 16 comme une entrée nommée "BOUTON"

LED = machine.Pin(18,machine.Pin.OUT)	# Déclaration d'un object sur la pin 18 comme une sortie nommée "LED"

while True: # boucle toujours vrai donc infinie pour un programme sans fin
    
   val = BUTTON.value() # Lecture de la valeur de l'object "BUTTON", la valeur renvoit l'état de l'entrée 1 ou 0.
    if val == 1:		# Comparaison de la valeur lue et d'une référence, ici 1, donc l'état haut.
        LED.value(1)	# Si la condition est validée la fonction value de l'object LED est appeler avec un argument pour définir la valuer de sortie de la pin liée.
    else:				# Mot clé pour si la condition n'est pas respecter
        LED.value(0)	# La sortie d'obejet est mise à zéro, donc mise à l'état bas.
