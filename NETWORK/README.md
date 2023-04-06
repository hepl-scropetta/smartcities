# Network

En MicroPython, le module network permet de configurer et de gérer les connexions réseau sans fil sur des microcontrôleurs compatibles. Ce module fournit des classes et des fonctions pour configurer et gérer des connexions Wi-Fi et Ethernet.

Les principales classes disponibles dans le module network sont :

+ `WLAN`: une classe permettant de configurer et de gérer les connexions Wi-Fi.
+ `LAN`: une classe permettant de configurer et de gérer les connexions Ethernet.
+ `Server`: une classe permettant de créer un serveur HTTP ou FTP.

Les principales fonctions disponibles dans le module network sont :

+ `WLAN.connect()`: une fonction permettant de se connecter à un réseau Wi-Fi.
+ `WLAN.disconnect()`: une fonction permettant de se déconnecter d'un réseau Wi-Fi.
+ `WLAN.isconnected()`: une fonction permettant de vérifier si la connexion Wi-Fi est active.
+ `LAN.active()`: une fonction permettant d'activer ou de désactiver la connexion Ethernet.
+ `LAN.ifconfig()`: une fonction permettant de configurer l'adresse IP, le masque de sous-réseau et la passerelle par défaut pour une connexion Ethernet.

Le module network est particulièrement utile pour les projets IoT (Internet des Objets) qui nécessitent une connexion réseau pour communiquer avec des serveurs ou des appareils distants.

## Module `ntptime`

Le module ntptime en MicroPython permet de synchroniser l'horloge temps réel d'un microcontrôleur avec l'heure universelle coordonnée (UTC) à l'aide du protocole Network Time Protocol (NTP). 

Les fonctions disponibles dans ce module sont les suivantes :

+ `settime()` : Met à jour l'horloge temps réel du microcontrôleur en utilisant l'heure UTC récupérée à partir d'un serveur NTP.
+ `time()` : Retourne l'heure UTC en secondes depuis l'époque Unix (1er janvier 1970).
+ `host2ntp(host)` : Convertit une adresse IP ou un nom de domaine en une adresse NTP.
+ `ntpc` : Objet de configuration pour le client NTP.
+ `NTP_DELTA` : Constante pour compenser le décalage de temps.
+ `NTP_PACKET_FORMAT` : Format de la trame de requête NTP.

## Module `socket`

Le module socket en MicroPython permet de communiquer avec des protocoles réseau tels que `TCP`, `UDP`, `SSL`, etc. Il fournit une interface compatible avec la bibliothèque standard Python pour créer et gérer des sockets. 

Les fonctions disponibles dans ce module sont les suivantes :

+ `socket(family, type, proto=0)` : Crée un nouveau socket avec une famille d'adresses et un type de socket spécifiés.
+ `bind(address)` : Associe le socket à une adresse.
+ `listen(backlog)` : Met le socket en mode écoute.
+ `accept()` : Accepte une connexion entrante.
+ `connect(address)` : Établit une connexion avec une adresse distante.
+ `send(bytes)` : Envoie des données à l'autre extrémité de la connexion.
+ `recv(bufsize)` : Reçoit des données depuis l'autre extrémité de la connexion.
+ `setblocking(flag)` : Configure le mode bloquant ou non bloquant du socket.
+ `settimeout(value)` : Définit le délai d'attente pour les opérations de socket.
+ `close()` : Ferme le socket.
+ `getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)` : Résout une adresse de serveur et renvoie une liste de tuples contenant les informations d'adresse.
+ `gethostname()` : Renvoie le nom d'hôte local.
+ `gethostbyname(hostname)` : Renvoie l'adresse IP correspondant à un nom d'hôte donné.
+ `gethostbyaddr(ip_address)` : Renvoie le nom d'hôte correspondant à une adresse IP donnée.