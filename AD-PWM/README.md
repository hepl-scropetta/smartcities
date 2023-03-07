# AD-PWM

Nous retrouvons 4 codes dans ce répertoire qui permettent d'avoir un premier apperçu sur le `PWM`. Pour le Raspberry Pico W, la totalité de ses broches GPIO peut utilisé du `PWM`. Une explication du fonctionnent du `PWM` est reprise ci-dessous, dans ce document. Les codes de ce fichier utilisent cette technologie pour contrôler l'intensité d'une LED ainsi que la tonnalité d'un buzzer, en modifiant la fréquence ou le rapport cyclique.

## led_linear_dimming

Ce code [led_linear_dimming](led_linear_dimming.py) va jouer sur le rapport cyclique pour manipuler l'intensité de la LED. Ce code est simple. Après avoir initalisé un objet PWM qui sera notre LED, une boucle `for` avec un incrément de 0 à 20 modifie le cycle. Nous pouvons donc voir l'intensité de la LED augmenter progressivement puis s'éteindre.

## PWM_pot_led

Pour le code [PWM_pot_led](PWM_pot_led.py), c'est un potentiomètre qui va contrôler le signal `PWM`. Ce signal sera affiché dans la console et modifiera l'intensité de la LED branchée. Une nouvelle fonction est nécéssaire `read_u16()` qui lit la valeur du potentiomètre.

## musique

Le script [musique](musique.py) joue "La lettre à Elise" de Beethoven. Il ne compose que les 10 premières notes pour montrer l'utilisation de l'objet `PWM` connecté à un buzzer. Afin de créer la sonorité d'une note spécifique, il faut changer la fréquence de vibration du son. Le buzzer en vibrant génère un son.La fréquence est définie par le rapport cyclique de la sortie `PWM`. C'est la fonction `duty_16()`, expliquée [ici](#duty_u16), qui permet de définir la fréquence voulue.

## Pulse Width Modulation

Le PWM (Pulse Width Modulation) est une technique de modulation de largeur d'impulsion qui permet de contrôler la puissance fournie à un dispositif électrique en modifiant la durée des impulsions d'un signal numérique.

Le principe de fonctionnement du `PWM` consiste à produire un signal numérique dont le rapport cyclique (duty cycle) varie en fonction de la tension de commande. Le rapport cyclique est défini comme la proportion de temps pendant laquelle le signal est à l'état "haut" par rapport à la période totale du signal. Par exemple, si la période du signal est de 1 milliseconde et que le signal est à l'état "haut" pendant 0,5 milliseconde, le rapport cyclique est de 50 %. 
Le `PWM` peut être aussi utilisé pour limiter la consommation d'une LED sans différence visible. Pour ce faire, on joue sur des limites physiques du corps humain, et on lui faire croire que la LED est constament alimentée alors que physiquement elle clinote très rapidement.

## Fonction 

### `PWM.freq()`

La fonction `freq()` est une méthode de l'objet `PWM`. Cette méthode permet de configurer la fréquence de modulation de largeur d'impulsion (PWM) d'un signal.
En modifiant la fréquence de modulation de largeur d'impulsion, il est possible de contrôler la vitesse de variation du signal PWM et donc, le comportement du dispositif ou du circuit contrôlé.

### `duty_u16()`

La fonction `duty_u16` est utilisée pour modifier le rapport cyclique d'un signal PWM généré par l'objet `PWM`. Elle permet de préciser le rapport cyclique en utilisant une valeur entière de 16 bits plutôt qu'un pourcentage; ce qui peut être utile dans certaines applications où une résolution plus fine est nécessaire.

### `read_u16()`

La fonction `read_u16()` est une méthode de l'objet `ADC`. Cette méthode permet de lire la valeur numérique de la tension analogique mesurée par l'`ADC`, convertie en un entier non signé de 16 bits.
La valeur retournée par la méthode `read_u16()` est un entier non signé de 16 bits représentant la valeur numérique de la tension mesurée. Cette valeur est comprise entre `0` (correspondant à une tension de référence de 0 V) et `65535` (correspondant à une tension de référence maximale).
