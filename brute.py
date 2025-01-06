import requests 
#Permet de récupérer les arguments passés en ligne de commande.
import sys 

sub_list = open("subdomains.txt").read()
#splitlines() 
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        pass
    else:
        print("Valid domain: ",sub_domains)

#Pour lancer le programme donner 
#en terminal un nom de domaine exemple: python brute.py google 