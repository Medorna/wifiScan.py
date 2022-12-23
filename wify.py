# Importamos la librería Scapy y algunas otras librerías necesarias
import scapy.all as scapy
import os

# Creamos una función para escanear las redes WiFi


def scan_wifi():
    # Enviamos un paquete de broadcast para solicitar a los puntos de acceso que se identifiquen
    broadcast = scapy.Ether(dst="00000000000000000")
    wifi_probe_request = scapy.Dot11ProbeReq()
    packet = broadcast / wifi_probe_request
    iface = "Wi-Fi"

# Creamos una función de callback para procesar las respuestas de los puntos de acceso


def wifi_callback(packet):
    # Si el paquete es una respuesta de punto de acceso (subtype=5), procesamos la información
    if packet.haslayer(scapy.Dot11ProbeResp):
        # Extraemos la dirección MAC del punto de acceso y el nombre de la red (SSID)
        ap_mac = packet.addr2
        ap_name = packet.info

        # Mostramos la información en pantalla
        print(f"Dirección MAC: {ap_mac} | SSID: {ap_name}")


# Creamos un bucle para escanear las redes WiFi cada 5 segundos
while True:
    scan_wifi()
    scapy.sniff(iface="Wi-Fi", prn=wifi_callback, store=0)
