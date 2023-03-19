# LCD

Ce répertoire nous permet d'apprendre le comportement d'un afficheur LCD (Liquide Crystal Display). Vous trouverez trois codes. Le premier permet simplement d'afficher un message. Le deuxième dévellope l'idée de récupérer une donnée, dans notre cas la valeur d'une entrée analogique avec un potentiomètre. Et le troisième, la lecture de la température et de l'humidité, via un module DHT22, et afficher les données sur l'écran.

## LCD_hello_world

Programme simple pour débuté avec le LCD. Déclaration d'un object LCD, via un [module importé](#module-externe) d'internet. Ensuite, quelques lignes de paramètrage pour initialiser correctement l'object sont obligatoire. Pour afficher quelques chose, on place le curseur en début de ligne, à l'aide de la fonction [`setCursor()`](#setCursor). La fonction [`print()`](#print) premet d'envoyer une chaîne de caractères.

## LCD + POT

Ce [code](LCD+POT.py) importe des modules nécessaires pour le contrôle d'un afficheur LCD1602, un capteur de température et d'humidité DHT11, un capteur de rotation à angle variable, un module `I2C` pour la communication et un module `PWM` pour la génération de signaux de modulation de largeur d'impulsion. Il initialise ensuite le capteur de rotation, l'afficheur LCD et entre dans une boucle while infinie. À chaque itération, il lit la valeur du capteur de rotation, l'affiche sur l'afficheur LCD et attend une seconde avant de répéter le processus.

## LCD + TEMP

Ce [code](LCD+TEMP.py) importe les modules nécessaires pour le contrôle d'un afficheur LCD1602, un capteur de température et d'humidité DHT11, un module I2C pour la communication et un module PWM pour la génération de signaux de modulation de largeur d'impulsion. Il initialise ensuite le capteur de température et d'humidité, l'afficheur LCD et crée deux caractères personnalisés pour afficher le symbole du pourcentage et le symbole du degré Celsius.

Ensuite, il entre dans une boucle while infinie. À chaque itération, il effectue une mesure de la température et de l'humidité à l'aide du capteur DHT11, puis affiche ces valeurs sur l'afficheur LCD en utilisant les caractères personnalisés créés précédemment pour afficher les symboles de pourcentage et de degré Celsius. Il attend ensuite une demi-seconde avant de répéter le processus.

## Module externe
Le module de base machine ne contient pas tout les modules possibles. Pour utiliser un module externe, il faut importer le fichier du module, avec la déclarration de la classe, sur le pico. Les éditeurs de micropython permettent de téléverser le ficher sur le microcontrôller facilement.

## Fonction 

### `setCursor()`

Cette fonction permet de définir la position du curseur sur l'afficheur LCD. La fonction `setCursor()` prend deux arguments : la colonne et la ligne où le curseur doit être positionné. Les valeurs de colonne et de ligne sont des entiers, où la colonne et la ligne sont indexées à partir de zéro. 

### `print()`

Cette fonction très utilisée dans beaucoup de librairie affiche un message. Le message est donné en argument dans la fonction. Dans notre cas le message sera envoyer vers le LCD. 

### Toute les fonctions du module `LCD1602`

- `__init__(self, i2c, cols, rows)` : initialise l'afficheur LCD avec les arguments spécifiés, où i2c est le canal I2C utilisé, cols est le nombre de colonnes de l'afficheur et rows est le nombre de lignes de l'afficheur.
- `clear(self)` : efface l'afficheur LCD.
- `home(self)` : ramène le curseur de l'afficheur LCD en haut à gauche.
- `display(self)` : active l'affichage de l'afficheur LCD.
- `no_display(self)` : désactive l'affichage de l'afficheur LCD.
- `cursor(self)` : active l'affichage du curseur de l'afficheur LCD.
- `no_cursor(self)` : désactive l'affichage du curseur de l'afficheur LCD.
- `blink(self)` : active le clignotement du curseur de l'afficheur LCD.
- `no_blink(self)` : désactive le clignotement du curseur de l'afficheur LCD.
- `scroll_display_left(self)` : fait défiler le contenu de l'afficheur LCD vers la gauche.
- `scroll_display_right(self)` : fait défiler le contenu de l'afficheur LCD vers la droite.
- `left_to_right(self)` : configure l'écriture de gauche à droite pour l'afficheur LCD.
- `right_to_left(self)` : configure l'écriture de droite à gauche pour l'afficheur LCD.
- `autoscroll(self)` : active la fonction de défilement automatique de l'afficheur LCD.
- `no_autoscroll(self)` : désactive la fonction de défilement automatique de l'afficheur LCD.
- `create_char(self, location, charmap)` : crée un caractère personnalisé pour l'afficheur LCD en utilisant les données spécifiées dans charmap.