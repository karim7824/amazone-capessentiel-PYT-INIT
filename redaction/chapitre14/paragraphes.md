# Chapitre 14 : Gestion des packages - import et création

Ce chapitre couvre l'organisation du code en modules et packages ainsi que la gestion des fichiers et répertoires en Python. Vous apprendrez à structurer vos projets, importer des bibliothèques et automatiser le déploiement d'environnements. Ces compétences sont essentielles pour créer des applications modulaires et maintenables.

Dans ce chapitre :

* Librairie et script pip
* Importation de package
* Contenu d'un package
* Chemin d'accès
* Packages standards os, os.path, pathlib et zlib
* Gestion des répertoires - mkdir, listdir, walk, move, rmdir
* Gestion des fichiers - open, read, write, seek, tell, zip
* Automatiser une installation avec gel et requirements.txt

---

## Librairie et script pip

L'outil `pip` permet d'installer, mettre à jour et supprimer des bibliothèques tierces issues du dépôt PyPI. Il s'exécute depuis le terminal ou via l'interpréteur Python pour gérer les dépendances du projet. Son utilisation garantit l'accès à un écosystème enrichi au-delà de la bibliothèque standard.

```bash
# Installation d'un package depuis le terminal
pip install requests

# Verification de la liste des packages installés
python -m pip list

```

> 💡 **Bonne pratique :** Exécutez toujours `pip` au travers de `python -m pip` pour vous assurer d'installer les paquets dans l'environnement Python actif.

---

## Importation de package

L'instruction `import` charge des modules externes ou locaux dans l'espace de nommage de votre script. On peut importer un module entier, des fonctions spécifiques ou utiliser un alias pour simplifier le code. Cela favorise la réutilisation du code sans redéfinition.

```python
# Import complet et utilisation avec alias
import math as m
print(m.sqrt(16))  # 4.0

# Import ciblé d'une fonction spécifique
from datetime import datetime
print(datetime.now())

```

> 💡 **Attention :** Évitez l'usage de `from module import *` car cela pollue l'espace de nommage et rend l'origine des fonctions floue.

---

## Contenu d'un package

Un package Python est un répertoire contenant des modules et un fichier spécial `__init__.py`. Ce fichier indique à Python que le dossier doit être traité comme un package réutilisable. Il permet d'initialiser le package et d'exposer les fonctionnalités principales.

```python
# Structure : mon_package/__init__.py
# Contenu de mon_package/outils.py
def saluer(nom):
    return f"Bonjour {nom}"

# Utilisation depuis le script principal
from mon_package.outils import saluer
print(saluer("Alice"))

```

> 💡 **Bonne pratique :** Depuis Python 3.3, le fichier `__init__.py` est optionnel (namespace packages), mais le conserver reste fortement conseillé pour la clarté de la structure.

---

## Chemin d'accès

Python recherche les modules importés dans la liste des répertoires définie par `sys.path`. Ce chemin inclut le répertoire du script courant, la bibliothèque standard et les paquets installés via `pip`. Il est possible d'inspecter ou de modifier dynamiquement cette liste si nécessaire.

```python
import sys

# Affichage des répertoires de recherche d'imports
for chemin in sys.path:
    print(chemin)

# Ajout temporaire d'un répertoire personnalisé
sys.path.append("/chemin/vers/mes_modules")

```

> 💡 **Attention :** Modifier `sys.path` directement dans le code peut rendre votre projet difficile à déployer ; préférez l'utilisation de variables d'environnement comme `PYTHONPATH`.

---

## Packages standards os, os.path, pathlib et zlib

La bibliothèque standard fournit des modules robustes pour interagir avec le système et compresser des données. Le module `pathlib` offre une approche orientée objet préférable à `os.path` pour manipuler les chemins. Le module `zlib` permet de compresser et décompresser des flux de données en mémoire.

```python
from pathlib import Path
import zlib

# Manipulation moderne de chemin avec pathlib
fichier = Path("donnees") / "rapport.txt"
print("Nom du fichier :", fichier.name)

# Compression de données avec zlib
texte = b"Donnees a compresser plusieurs fois..."
compresse = zlib.compress(texte)
print("Taille réduite :", len(compresse))

```

> 💡 **Bonne pratique :** Privilégiez l'utilisation de `pathlib.Path` plutôt que `os.path` pour une gestion interplateforme plus claire et élégante des chemins.

---

## Gestion des répertoires - mkdir, listdir, walk, move, rmdir

Le module `os` et l'utilitaire `shutil` permettent de manipuler l'arborescence des dossiers. Vous pouvez créer, lister, parcourir récursivement ou supprimer des répertoires. Ces fonctions sont essentielles pour l'automatisation des tâches d'administration système.

```python
import os
import shutil

# Création et listing d'un répertoire
os.mkdir("mon_dossier")
print("Contenu :", os.listdir("."))

# Déplacement/renommage et suppression
shutil.move("mon_dossier", "dossier_archive")
os.rmdir("dossier_archive")

```

> 💡 **Attention :** La fonction `os.rmdir()` échoue si le dossier n'est pas vide ; utilisez `shutil.rmtree()` pour tout supprimer de manière récursive.

---

## Gestion des fichiers - open, read, write, seek, tell, zip

L'instruction `open()` permet de manipuler les fichiers en lecture ou écriture avec gestion du curseur via `seek()` et `tell()`. Le gestionnaire de contexte `with` garantit la fermeture automatique du fichier. Le module `zipfile` permet de créer et d'extraire des archives compressées.

```python
import zipfile

# Écriture, positionnement du curseur et lecture
with open("test.txt", "w+") as f:
    f.write("Ligne de test")
    f.seek(0)  # Replacer le curseur au début
    print("Contenu :", f.read())

# Création d'une archive zip
with zipfile.ZipFile("archive.zip", "w") as zf:
    zf.write("test.txt")

```

> 💡 **Bonne pratique :** Utilisez toujours le bloc `with open(...)` pour vous assurer que les descripteurs de fichiers sont libérés même en cas d'erreur.

---

## Automatiser une installation avec gel et requirements.txt

Le mécanisme de "freeze" extrait la liste exacte des dépendances installées avec leurs versions. L'enregistrement dans un fichier `requirements.txt` permet de reproduire l'environnement à l'identique. Cela assure la portabilité de votre projet sur un autre serveur ou poste développeur.

```bash
# Génération du fichier des dépendances
python -m pip freeze > requirements.txt

# Installation des dépendances sur un autre environnement
python -m pip install -r requirements.txt

```

> 💡 **Bonne pratique :** Effectuez la génération de `requirements.txt` au sein d'un environnement virtuel propre (`venv`) pour éviter d'inclure des paquets inutiles du système.

---

## Synthèse du chapitre

```python
import sys
from pathlib import Path
import zipfile

def archiver_projet(dossier_source, nom_zip):
    """Parcourt un dossier et compresse son contenu dans une archive ZIP."""
    chemin_src = Path(dossier_source)
    fichier_zip = Path(nom_zip)

    if not chemin_src.exists():
        print(f"Erreur : Le dossier {dossier_source} n'existe pas.", file=sys.stderr)
        return False

    with zipfile.ZipFile(fichier_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for element in chemin_src.rglob("*"):
            if element.is_file():
                zf.write(element, element.relative_to(chemin_src))
    
    print(f"Archive créée : {fichier_zip.resolve()}")
    return True

# Application opérationnelle
archiver_projet(".", "sauvegarde.zip")

```

---

### Exercices de fin de chapitre

1. **Exercice 1 :** Écrivez un script Python qui crée un dossier nommé `export`, y génère un fichier texte `notes.txt` contenant trois lignes de votre choix, puis affiche la taille du fichier à l'écran.
2. **Exercice 2 :** Créez une fonction qui accepte le chemin d'un répertoire en paramètre, liste tous les fichiers `.py` présents dans ce dossier, puis génère une archive `modules.zip` les regroupant tous.
