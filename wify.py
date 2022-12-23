# Importamos las librerías necesarias
import scapy.all as scapy
import os
from time import sleep

# Creamos una función de callback para procesar las respuestas de los puntos de acceso


def wifi_callback(packet):
    # Si el paquete es una respuesta de punto de acceso (subtype=5), procesamos la información
    if packet.haslayer(scapy.Dot11ProbeResp):
        # Extraemos la direccion MAC del punto de acceso y el nombre de la red (SSID)
        mac = packet.addr2
        ssid = packet.info.decode()

        # Mostramos la información en pantalla
        print(f"Dirección MAC: {mac} | SSID: {ssid}")


        # Creamos un bucle para escanear las redes WiFi cada 5 segundos
# Creamos un bucle para escanear las redes WiFi cada 5 segundos
while True:
    # Enviamos un paquete de broadcast para solicitar a los puntos de acceso que se identifiquen
    broadcast = scapy.Ether(dst="00000000000000000")
    wifi_probe_request = scapy.Dot11ProbeReq()
    packet = broadcast / wifi_probe_request

    # Enviamos el paquete de broadcast y procesamos las respuestas de los puntos de acceso
    ans, _ = scapy.sr(packet, iface="Wi-Fi", timeout=1)
    for packet in ans:
        wifi_callback(packet)

    # Detenemos la ejecución durante 5 segundos
    sleep(5)