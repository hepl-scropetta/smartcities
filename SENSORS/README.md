# Sensor

## DHT11

Le capteur DHT11 est un capteur d'humidité et de température très utilisé en électronique et en domotique. Il est capable de mesurer la température ambiante et l'humidité relative de l'air. Ce capteur utilise un protocole de communication numérique à un seul fil pour transmettre les données au microcontrôleur.

Le module `dht` en MicroPython permet de communiquer avec le capteur DHT11 et de récupérer les données qu'il mesure.

Les fonctions disponibles dans ce module sont les suivantes :

+ `DHT11(pin)` : Crée une instance de capteur DHT11 en spécifiant le numéro de broche du microcontrôleur sur lequel il est connecté.
+ `measure()` : Mesure la température et l'humidité et renvoie les valeurs sous forme de tuple.
+ `temperature()` : Mesure et renvoie la température en degrés Celsius.
+ `humidity()` : Mesure et renvoie l'humidité relative en pourcentage.

Il convient de noter que le capteur DHT11 peut être assez lent, donc lors de la mesure, le microcontrôleur doit attendre que le capteur ait fini de transmettre les données. Pour cette raison, il est important de respecter les temps de pause recommandés entre les mesures pour éviter de corrompre les données.

## Microphone

Le microphone se branche sur une broche GPIO du Raspberry Pi Pico pour fournir une entrée audio analogique.

Une fois connecté, il est possible de lire les données audio à l'aide d'un script MicroPython. Le module `machine` peut être utilisé pour configurer le port GPIO connecté au microphone en tant que canal ADC et pour lire les données audio.

Il est également possible d'utiliser des bibliothèques tierces telles que PyAudio pour traiter les données audio lues à partir du microphone et effectuer des tâches telles que la reconnaissance vocale ou la détection de motifs sonores.

Notre code [microphone](microphone.py) nous utilisons le microphone comme un simple object `ADC` et donc on ne peut lire que la tension et l'afficher de 0 à 65535.

## Luminosité

Ce capteur renvoit simplement une tension qui défini la luminosité. Nous allons donc le virtualisé en un object `ADC` ensuite lire la valeur en 16 bits. Cette valeur peut être utilisé pour définir des conditions et des régles en fonction de la lumière.

## PIR (Passive Infrared Sensor)

Les capteurs PIR sont des capteurs utilisés pour détecter les mouvements. Ils détectent les changements de température dans leur champ de vision, ce qui leur permet de détecter les mouvements des personnes ou des animaux.

Le fonctionnement des capteurs PIR est basé sur le principe de la détection infrarouge passive. Ils sont composés d'un pyroélément qui convertit les variations de température en signaux électriques. Lorsqu'une personne ou un animal se déplace dans le champ de vision du capteur, il émet une quantité de chaleur différente de celle de l'environnement, ce qui déclenche une variation de température et un signal électrique est produit par le pyroélément.

Ce [code](PIR.py) utilise un capteur PIR connecté à la broche 20 pour détecter des mouvements. Lorsqu'un mouvement est détecté, la LED connectée à la broche 25 s'allume pendant 10 secondes. Ensuite, la LED s'éteint et le code retourne en attente de détection de mouvements.