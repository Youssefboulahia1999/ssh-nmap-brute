🛠️ Python Security Toolkit

Une collection de trois scripts Python essentiels pour les tests d'intrusion : Brute Scanner, Port Scanner, et SSH Brute Force Attack.

📚 1. Brute Scanner

📋 Description
Ce script identifie les sous-domaines actifs d'un domaine cible en utilisant une liste pré-définie de sous-domaines. Chaque sous-domaine est vérifié par une requête HTTP, et seuls les sous-domaines valides sont affichés.

🚀 Fonctionnalités
Lecture d'une liste de sous-domaines depuis un fichier (subdomains.txt).
Vérification des sous-domaines via des requêtes HTTP.
Affichage des sous-domaines actifs.
🛠️ Prérequis
Python 3.x
requests
Installez la bibliothèque avec :

pip install requests
💻 Utilisation
Préparez un fichier subdomains.txt avec une liste de sous-domaines (un par ligne).
Lancez le script :
python scanner.py example.com
Remplacez example.com par le domaine cible.

📂 Structure du Projet
├── subdomains.txt  # Liste des sous-domaines
├── scanner.py      # Script principal
🛠️ 2. Pentester - Port Scanner

📋 Description
Un scanner de ports TCP conçu pour analyser une adresse IP spécifique afin de détecter les ports ouverts.

🚀 Fonctionnalités
Scan des ports de 1 à 65535.
Timeout optimisé pour des scans rapides.
Affichage clair des résultats avec une bannière ASCII générée par Pyfiglet.
🛠️ Prérequis
Python 3.x
pyfiglet
Installez la bibliothèque avec :

pip install pyfiglet
💻 Utilisation
Modifiez l'adresse IP directement dans le script :
ip = '192.12.1.1'
Lancez le script :
python port_scanner.py
📊 Exemple de sortie
192.12.1.1 
Python 4 Pentester
Port Scanner

Open Ports are:
22, 80, 443
📂 Structure du Projet
├── port_scanner.py  # Script principal
🔒 3. SSH Brute Force Attack

📋 Description
Un script automatisé pour effectuer une attaque par force brute sur un serveur SSH en utilisant une liste de mots de passe.

🚀 Fonctionnalités
Connexion SSH automatisée.
Chargement d'une liste de mots de passe depuis un fichier texte.
Gestion des erreurs d'authentification.
Affichage des tentatives de connexion et du mot de passe valide trouvé.
🛠️ Prérequis
Python 3.x
paramiko
pwntools
Installez les bibliothèques avec :

pip install paramiko pwntools
💻 Utilisation
Préparez un fichier texte avec une liste de mots de passe (small.txt).
Modifiez les paramètres du script :
host = '192.12.1.1'
username = 'kali'
Lancez le script :
python ssh_bruteforce.py
📊 Exemple de sortie
[0] Attempting password: '123456' !
[X] Invalid password
[1] Attempting password: 'password' !
[>] Valid password found: 'admin123'!
📂 Structure du Projet
├── ssh_bruteforce.py  # Script principal
├── small.txt          # Fichier de mots de passe
