#Permet de récupérer les arguments passés en ligne de commande.
import sys
# Permet la communication réseau et l'ouverture de connexions TCP/IP.
import socket
# Pyfiglet : Affiche un texte stylisé en ASCII.
import pyfiglet
ascii_banner = pyfiglet.figlet_format("192.168.1.197 \n Python 4 Pentester\nPort Scanner")
print(ascii_banner)

#address ip de la machine a scanner
ip = '192.168.1.197'
open_ports =[]

ports = range(1,65535)

def probe_port(ip,port,result = 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip,port))
        if r == 0:
            result = r
            sock.close()
    except Exception as e:
        pass
    return result
for port in ports:
    sys.stdout.flush()
    response = probe_port(ip,port)
    if response ==0:
        open_ports.append(port)

if open_ports:
    print ("Open Ports are:")
    print (sorted(open_ports))
else:
    print ("Looks like no ports are open:")