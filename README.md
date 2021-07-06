# OC_P4
---
### *Chess game project*


# 1. Description du programme
---
Le programme Chess game permet de créer des tournois composés de plusieurs rounds eux-même contenant plusieurs matchs, puis d'y indiquer les résultats. Le programme génère automatiquement les différentes rencontres selon les règles du tournoi Suisse.
Le programme permet également de créer, gérer et afficher les différents joueurs et peut également afficher les tournois terminés.


# 2. Créer l'environnement virtuel puis l'activer
---
#### Windows :
* Créer l'environnement virtuel avec la commande du terminal suivante : "python -m venv env"
* Activer l'environnement virutel depuis le terminal grâce à la commande suivante : "env/scripts/activate"
#### Unix :
* Créer l'environnement virtuel avec la commande du terminal suivante : "virtutalenv -p env venv"
* Activer l'environnement virutel depuis le terminal grâce à la commande suivante : "source env/bin/activate"


# 3. Importer les modules
---
#### Modules utilisés dans le programme :
* import json
* import datetime
* import re
* import enum
* import random
* from itertools import combinations
* from typing import Union
Le programme a été prévu pour tourner sous Python 3.9.5.
Les bibliothèques et modules listés ci-dessus sont tous déjà incluts avec cette version de python.

#### Installer le fichier requirements sur Windows et Unix :
Utilisez la commande : " pip install -r requirements.txt "


# 4. Installer et Initialiser le git
---
* Si vous n'avez pas encore git, cliquer sur le lien suivant : [Installer git](https://git-scm.com/downloads) et suivez les instructions du site.
* Initialiser ensuite le git avec la commande suivante dans votre console (assurez-vous que vous vous situez bien dans le dossier qui va contenir votre projet avant de lancer la commande): " *git init* " (Fonctionne pour Windows et Unix)


# 5. Importer le projet depuis github
---
Veuillez taper la commande suivante dans votre console : " *git clone https://github.com/GuillaumeP29/OC_P4.git* "


# 6. Créer les fichiers JSON
---
Pour assurer le bon fonctionnement du programme, veuillez créer le dossier et les fichiers suivants :
* Un dossier nommé : " *JSON* ".
##### Et dans ce dossier :
* Un fichier nommé : " *tournaments.json* "
* Un fichier nommé : " *players.json* "


# 7. Lancer le programme
---
Il ne vous reste plus qu'à lancer le programme depuis la console à l'aide de la commande : " *python main.py* "