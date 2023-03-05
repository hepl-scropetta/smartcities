# smartcities

## Introduction

Ce répertoire rentre dans le cadre d'un cours d'apprentissage de la programmation en MicroPython sur des Raspberry Pico W. Une série de code spécifique à l'utilisation de capteur, d'affichage et de communication divers est demander. Vous retrouvez ces codes dans les différents répertoires.

## Raspberry Pico

Le Raspberry Pi Pico W est un microcontrôleur doté d'un processeur ARM Cortex-M0+ et d'une mémoire flash de 4 Mo. Il est équipé d'un module Wi-Fi intégré, ce qui lui permet de se connecter facilement à un réseau sans fil et de communiquer avec d'autres périphériques IoT.
Le Pico W est également doté de nombreuses interfaces d'E/S, notamment des broches GPIO (General Purpose Input/Output), des interfaces SPI (Serial Peripheral Interface), I2C (Inter-Integrated Circuit), UART (Universal Asynchronous Receiver/Transmitter) et PWM (Pulse Width Modulation).
Le Pico W est compatible avec MicroPython, C/C++ et d'autres langages de programmation, ce qui le rend facile à programmer et adapté aux besoins des développeurs de différents niveaux de compétence.
Parmi les autres fonctionnalités intéressantes du Pico W, on peut citer sa faible consommation d'énergie, qui le rend adapté aux applications alimentées par batterie, et sa taille compacte, qui le rend facilement intégrable dans des projets.

Le Raspberry Pi Pico W dispose de plusieurs interfaces d'E/S, dont les suivantes :

- GPIO (General Purpose Input/Output) : Le Pico W dispose de 26 broches GPIO, qui peuvent être utilisées pour entrer ou sortir des signaux numériques. Ces broches peuvent être utilisées pour contrôler des périphériques tels que des LED, des boutons, des capteurs, des actionneurs, etc.

- I2C (Inter-Integrated Circuit) : Le Pico W dispose de deux broches I2C, SDA et SCL, qui peuvent être utilisées pour communiquer avec des périphériques externes tels que des capteurs, des écrans LCD, des horloges en temps réel, etc.

- SPI (Serial Peripheral Interface) : Le Pico W dispose de deux broches SPI, MOSI et MISO, ainsi que d'une broche de sélection d'esclave (SS) et d'une broche de signal d'horloge (SCK). Cette interface est couramment utilisée pour communiquer avec des périphériques tels que des écrans TFT, des cartes SD, des capteurs, etc.

- UART (Universal Asynchronous Receiver/Transmitter) : Le Pico W dispose de deux broches UART, TX et RX, qui peuvent être utilisées pour communiquer avec d'autres périphériques via une connexion série.

- PWM (Pulse Width Modulation) : Le Pico W dispose de trois broches PWM, qui peuvent être utilisées pour générer des signaux de modulation de largeur d'impulsion pour contrôler la vitesse de rotation des moteurs, la luminosité des LED, etc.

Voici une image avec toutes les entrées/sorties du Raspberry Pico W.

![Pinout Raspberry Pico](https://components101.com/sites/default/files/component_pin/Raspberry%20Pi-Pico-W-pinout.png)

### Test de consommation

Je posède un appareil qui permet de mesurer le courant et la tension d'une connection usb. Facile à trouver sur internet pour une quelque euro. J'étais étonnament surpris de voir que le Raspberry Pico W ne consomme que 18mA en fonctionnement classique (tester avec une simple boucle infini vide). Voilà une image de mon testeur:

<picture>
  <img alt="" src="https://user-images.githubusercontent.com/125206428/222976450-1ca953a4-7b56-4464-82bc-3817f03f78c5.JPG" height="200">  
</picture>

## Micropython

MicroPython est une implémentation du langage de programmation Python qui a été optimisé pour les microcontrôleurs et les systèmes embarqués. Il permet aux développeurs de créer des applications IoT (Internet of Things) avec une syntaxe familière et une grande facilité de développement.
Grâce à sa faible empreinte mémoire et à sa rapidité d'exécution, MicroPython est idéal pour les systèmes où les ressources sont limitées, tels que les microcontrôleurs basés sur ARM et les cartes de développement comme le Raspberry Pi.
Dans ce guide, nous allons apprendre les bases de MicroPython et comment l'utiliser pour créer des projets IoT. Nous allons également explorer les fonctionnalités avancées de MicroPython, telles que l'accès aux broches d'E/S, la communication avec des périphériques externes et la connexion à Internet.

## Thonny

Thonny est un environnement de développement intégré (IDE) pour Python qui est conçu pour faciliter l'apprentissage et l'enseignement de la programmation. Il est facile à utiliser pour les débutants en programmation, mais offre également des fonctionnalités avancées pour les développeurs expérimentés.

Les principales fonctionnalités de Thonny incluent :

- Interface utilisateur conviviale : Thonny est conçu pour être facile à utiliser et à comprendre pour les débutants en programmation. Il offre une interface utilisateur claire et intuitive qui facilite la création, l'exécution et le débogage de programmes Python.

- Éditeur de code intégré : Thonny dispose d'un éditeur de code intégré qui prend en charge la coloration syntaxique, la complétion automatique et l'indentation automatique. Il offre également une fonctionnalité de vérification d'erreur en temps réel qui aide à détecter les erreurs de syntaxe dans le code.

- Débogueur intégré : Thonny dispose d'un débogueur intégré qui permet de déboguer les programmes pas à pas, de définir des points d'arrêt et d'observer les variables en temps réel. Cette fonctionnalité est très utile pour identifier les erreurs de logique et de syntaxe dans le code.

- Gestionnaire de packages : Thonny dispose d'un gestionnaire de packages intégré qui permet d'installer et de mettre à jour les packages Python directement depuis l'interface utilisateur.

- Intégration avec les microcontrôleurs : Thonny prend en charge l'intégration avec plusieurs microcontrôleurs populaires, tels que le Raspberry Pi, le micro:bit, l'ESP8266, etc. Il offre une fonctionnalité de programmation en direct qui permet de télécharger le code directement sur le microcontrôleur et de le tester en temps réel.
