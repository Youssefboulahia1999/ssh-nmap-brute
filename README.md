🛠️ Brute Scanner

📚 Description

Ce script Python permet d'identifier les sous-domaines actifs d'un domaine cible en utilisant une liste pré-définie de sous-domaines.

Il vérifie chaque sous-domaine de la liste en effectuant une requête HTTP et affiche ceux qui répondent correctement.

🚀 Fonctionnalités

Lecture d'une liste de sous-domaines depuis un fichier (subdomains.txt).

Vérification de chaque sous-domaine via une requête HTTP.

Affichage des sous-domaines valides.

🛠️ Prérequis

Assurez-vous d'avoir installé :

Python 3.x

Bibliothèque requests

Vous pouvez installer requests avec pip :

pip install requests

📂 Structure du Projet

├── subdomains.txt  # Liste des sous-domaines à tester
├── scanner.py      # Script principal

💻 Utilisation

Préparez un fichier subdomains.txt contenant une liste de sous-domaines (un par ligne).

Lancez le script avec la commande suivante :

python scanner.py example.com

Remplacez example.com par le domaine cible.



🛠️ Pentester - Port Scanner

Ce projet est un scanner de ports simple écrit en Python. Il permet de vérifier les ports ouverts sur une adresse IP spécifique afin d'analyser la surface d'attaque d'une machine cible.

📋 Description

Le programme scanne les ports d'une adresse IP donnée.

Utilise le protocole TCP pour établir des connexions.

Affiche les ports ouverts après analyse.

Intègre une bannière ASCII générée avec Pyfiglet pour une présentation stylisée.

🛠️ Prérequis

Assurez-vous d'avoir installé les bibliothèques suivantes :

Python 3.x

Pyfiglet

Installation des dépendances :

pip install pyfiglet

🚀 Utilisation

Modifiez l'adresse IP dans le script Python :

ip = '192.168.1.197'

Exécutez le script :

python port_scanner.py

⚙️ Fonctionnement du script

Bannière ASCII : Une bannière est affichée au lancement du script.

Scan des ports : Les ports de 1 à 65535 sont testés.

Timeout court : Chaque port est sondé avec une limite de temps de 0,5 seconde.

Affichage des résultats : Les ports ouverts sont affichés dans la console.

📊 Exemple de sortie

192.168.1.197
Python 4 Pentester
Port Scanner

Open Ports are:
22, 80, 443


