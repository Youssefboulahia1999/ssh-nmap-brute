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

