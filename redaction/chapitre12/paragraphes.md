# Chapitre 12 : Gestion des package - import et création

La gestion des packages et des modules permet d'organiser et de structurer le code en composants réutilisables tout en exploitant la bibliothèque standard de Python. Maîtriser ces outils est indispensable pour industrialiser vos projets.
Dans ce chapitre :

* Librairie, scripts `pip` et importation de packages


* Contenu d'un package et gestion des chemins d'accès


* Packages standards (`os`, `os.path`, `path` et `zlib`)


* Gestion des répertoires et des fichiers


* Automatisation d'installation avec `gel` et `requirements.txt`


---

## librairie et script pip

Les scripts et librairies gérés via `pip` permettent d'installer, de maintenir et de partager des dépendances logicielles tierces au sein de vos environnements de développement.

```python
# Exemple de commande d'installation via pip (à exécuter dans le terminal)
# pip install package_name

```

> 💡 Utilisez toujours des environnements virtuels isolés pour vos projets afin d'éviter les conflits de versions entre les différentes bibliothèques tierces installées.

---

## importation de package

L'importation de modules ou de packages s'effectue à l'aide des instructions `import` ou `from ... import` pour intégrer des fonctionnalités externes dans vos scripts.

```python
# Importation d'un module standard ou tiers
import math
racine = math.sqrt(16)

```

> 💡 Évitez les importations globales du type `from module import *` pour préserver la lisibilité de votre espace de noms et éviter les conflits de noms de variables.

---

## Contenu d'un package

Un package en Python est un répertoire contenant un fichier d'initialisation (`__init__.py`) et plusieurs modules sous forme de fichiers source, permettant de structurer une application modulaire.

```python
# Structure logique d'un appel à un sous-module de package
# from mon_package import mon_module

```

> 💡 Le fichier `__init__.py` (qui peut être vide dans les versions récentes de Python) indique explicitement à l'interpréteur que le dossier doit être traité comme un package.

---

## chemin d'accès

La gestion des chemins d'accès permet de localiser avec précision les fichiers et répertoires sur le disque dur, garantissant la portabilité de vos scripts d'un système à un autre.

```python
import os

# Récupération du chemin absolu du répertoire courant
chemin_courant = os.getcwd()

```

> 💡 Privilégiez l'utilisation du module moderne `pathlib` pour manipuler les chemins d'accès de manière orientée objet et indépendante du système d'exploitation.

---

## package standards os, os.path, path et zlib

La bibliothèque standard de Python intègre de nombreux modules puissants comme `os`, `os.path` et `zlib` pour interagir avec le système d'exploitation et compresser des données.

```python
import os.path

# Vérification de l'existence d'un fichier
existe = os.path.exists("config.json")

```

> 💡 Explorez d'abord la bibliothèque standard avant d'installer des packages tiers, car elle couvre déjà la majorité des besoins basiques en manipulation système.

---

## Gestion des répertoires - mkdir, listdir, walk, move, rmdir

La manipulation des répertoires permet de créer, parcourir, déplacer ou supprimer des dossiers de manière automatisée au sein de vos scripts.

```python
import os

# Création d'un nouveau répertoire de travail
os.makedirs("nouveau_dossier", exist_ok=True)

```

> 💡 Utilisez l'argument `exist_ok=True` lors de la création de dossiers pour éviter de déclencher une exception si le répertoire existe déjà.

---

## Gestion des fichiers - open, read, write, seek, tell, zip

La gestion des fichiers bas niveau permet d'ouvrir, de lire, d'écrire, de positionner le curseur (`seek`, `tell`) et de manipuler des archives compressées (`zip`).

```python
# Ouverture et écriture sécurisée dans un fichier texte
with open("journal.txt", "w", encoding="utf-8") as f:
    f.write("Premier message de journalisation.")

```

> 💡 Utilisez toujours le gestionnaire de contexte `with` pour l'ouverture des fichiers afin de garantir leur fermeture automatique, même en cas d'erreur.

---

## Automatiser une installation avec gel et requirements.txt

L'automatisation du déploiement s'appuie sur un fichier `requirements.txt` listant les dépendances exactes du projet, facilitant leur réinstallation en une seule commande.

```bash
# Commande pour installer toutes les dépendances d'un projet
pip install -r requirements.txt

```

> 💡 Mettez régulièrement à jour votre fichier `requirements.txt` pour refléter fidèlement l'état de vos dépendances de développement.

---

## Exemple de synthèse

```python
import os
import os.path
import zlib

def preparer_environnement_projet(nom_dossier):
    """Crée un répertoire de travail, écrit un fichier de log et vérifie sa présence."""
    # 1. Gestion des répertoires : création sécurisée
    os.makedirs(nom_dossier, exist_ok=True)
    
    chemin_fichier = os.path.join(nom_dossier, "donnees.txt")
    
    # 2. Gestion des fichiers : écriture de données
    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        fichier.write("Contenu critique à compresser et archiver.")
        
    # 3. Utilisation de packages standards (vérification et compression zlib)
    if os.path.exists(chemin_fichier):
        with open(chemin_fichier, "rb") as fichier_1:
            donnees_brutes = fichier_1.read()
            donnees_compressees = zlib.compress(donnees_brutes)
            print(f"Taille originale : {len(donnees_brutes)} octets")
            print(f"Taille compressée : {len(donnees_compressees)} octets")

# Appel de la fonction de synthèse
preparer_environnement_projet("stock_donnees")

```

## Exercices

1. **Exercice 1 :** Écrivez un script qui utilise le module `os` pour lister tous les fichiers présents dans le répertoire courant.
2. **Exercice 2 :** Créez un fichier texte, écrivez-y une phrase, puis utilisez le module `zlib` pour compresser son contenu textuel lu en mode binaire.