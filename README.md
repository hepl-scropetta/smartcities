# smartcities

## Introduction

Ce répertoire rentre dans le cadre d'un cours d'apprentissage de la programmation en MicroPython sur des Raspberry Pico W. Une série de code spécifique à l'utilisation de capteur, d'affichage et de communication divers est demander. Vous retrouvez ces codes dans les différents répertoires.

## Raspberry Pico

Ce modèdle de Raspberry est conçu pour la programmation embarqué car il ne posède pas de système d'opération comme les Raspberry traditionnels. Il est beaucoup plus petit et surtout ça consommation est bien moindre, pour optimiser son utilisation lorsqu'il est branché sur une batterie. 
Ce modèle posède moins d'interface complexe comme des ports usb (type A) ou des ports graphique, comme les ports HDMI. Car il ne posède pas d'interface graphique pour afficher sur un écran. Par contre, il dispose de suffisament d'entrées/sorties GPIO pour les applications pour les quels, il à été consu pour. Ces GPIO ont tout de même des interfaces comme le I2C, SPI ou UART.

Voici une image avec les différentes fonctionnalité de toutes les entrées/sorties du Raspberry Pico W.

![Pinout Raspberry Pico](https://components101.com/sites/default/files/component_pin/Raspberry%20Pi-Pico-W-pinout.png)

Le Raspberry Pico est un microcontroller sera veut dire qu'il est composer de touts les éléments néssaisaire pour fonctionner par lui-même. Il pocède un microprocesseur ainsi que de la mémoire vive et de la mémoire morte. Le système est donc pratiquement entiérement intégrer, ajout de bouton et de connecter sur la carte simplifie sont utilisation lors de la programmation.

## Micropython

Ce langague de programmation sera utiliser pour programmer sur un microcontroller. Le langague dérive du Python mais est orienter pour les systèmes embarqués. On retrouve des modules conçus spécialement pour descendre de niveau et avoir acces facilement au hardware de la carte. 

## Thonny
