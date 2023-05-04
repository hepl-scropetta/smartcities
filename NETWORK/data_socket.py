import machine
import network
import ujson as json
import utime
from machine import Pin
from socket import socket

# Définir les paramètres du réseau
SSID = "WiFi-2.4-B4E5"
PASSWORD = "185E23AC26"

# Configurer la connexion Wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
while not wlan.isconnected():
    pass

print("Connecté au réseau Wifi on this IP: {}".format(str(wlan.ifconfig()[0])))

# Configurer le port et les broches
PORT = 8080
LED = Pin(25, Pin.OUT)

rep_ok = 'HTTP/1.1 200 OK '
rep_ok += 'Content-Type: application/json '
rep_ok += 'Content-Length: 20'

# Créer une fonction pour traiter les requêtes
def handle_request(request):

    response = {}
    response["status"] = 200
    response["data"] = {}
    try:
        # Parser la requête en JSON
        data = json.loads(request)
        
        # Lire les données
        value = data.get("value")
        
        # Traiter les données
        if value == "on":
            LED.on()
            response["data"]["message"] = "La LED a été allumée"
        elif value == "off":
            LED.off()
            response["data"]["message"] = "La LED a été éteinte"
        else:
            response["status"] = 400
            response["data"]["message"] = "Valeur invalide"
    except Exception as e:
        response["status"] = 500
        response["data"]["message"] = "Erreur : {}".format(str(e))
    
    # Encoder la réponse en JSON
    response = json.dumps(response)
    
    return response

# Configurer le serveur
server = socket()
server.bind(('', PORT))
server.listen(1)
print("Serveur démarré sur le port", PORT)

# Attendre les connexions et traiter les requêtes
while True:
    client, address = server.accept()
    print("Client connecté :", address)
    
    request = client.recv(1024)
    request = client.recv(1024)  # recevoir la requête des données

    request = str(request, "utf-8")
    print("Requête reçue :", request)
    
    response = handle_request(request)
    
    print("Réponse envoyée :", rep_ok)
    client.send(rep_ok)
    # client.sendall(bytes(response, "utf-8"))
    
    client.close()
