# NeoPixel

Le module neopixel en MicroPython permet de contrôler des bandes de LED adressables individuellement telles que les bandes NeoPixel ou WS2812. Il fournit une classe `NeoPixel` pour configurer et contrôler les bandes de LED, en utilisant des signaux de modulation de largeur d'impulsion (PWM) pour générer des couleurs. 

Les fonctions disponibles dans ce module sont les suivantes :

+ `neopixel.NeoPixel(pin, n, bpp=3, timing=True)` : Crée une instance de la classe NeoPixel avec les paramètres spécifiés.
+ `__setitem__(self, index, value)` : Définit la couleur de la LED à l'index spécifié avec la valeur spécifiée.
+ `fill(self, color)` : Définit la couleur de toutes les LEDs de la bande à la valeur spécifiée.
+ `write(self)` : Envoie la séquence de données pour mettre à jour les couleurs des LEDs de la bande.
+ `brightness(self, brightness)` : Définit la luminosité de la bande de LED.
+ `get(self, index)` : Retourne la couleur de la LED à l'index spécifié.
+ `__len__(self)` : Retourne le nombre de LED dans la bande.


Ce [code](pixel_color.py) est une démonstration des possibilités avec une bande de NeoPixel. La bibliothèque `neopixel` est importée pour créer l'objet `np` représentant la bande de pixels, connectée au GPIO 4 du microcontrôleur. La fonction `demo()` est définie pour faire défiler différents effets de lumière sur la bande de pixels, tels que des cycles de couleurs, des rebonds et des transitions de fondu. La boucle `while True` exécute en continu la fonction `demo()` pour faire défiler les différents effets sur la bande de pixels.