# Chapitre 14 : Gestion des packages - import et création

Ce chapitre couvre l'organisation du code en modules et packages ainsi que la gestion des fichiers et répertoires en Python. Vous apprendrez à structurer vos projets, importer des bibliothèques et automatiser le déploiement d'environnements. Ces compétences sont essentielles pour créer des applications modulaires et maintenables.

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
# Installation d'un package depuis le terminal au moyen de pip
pip install requests  # si pip est un executable
python -m pip install requests # en passant par pip en tant que module

# Verification de la liste des packages installés et les versions
python -m pip list

# Détail sur un package
pip show jsonpickle
Name: jsonpickle
Version: 4.1.2
Summary: jsonpickle encodes/decodes any Python object to/from JSON
Home-page: https://jsonpickle.readthedocs.io/
Author: Theelx
Author-email: David Aguilar <davvid+jsonpickle@gmail.com>
License: BSD-3-Clause
Location: C:\Program Files\Python312\Lib\site-packages
Requires:
Required-by:

```
**Commandes principales de `pip`**

| Commande | Description | Exemple |
| --- | --- | --- |
| **`pip install <pkg>`** | Installe un paquet depuis PyPI | `pip install requests` |
| **`pip uninstall <pkg>`** | Désinstalle un paquet | `pip uninstall requests` |
| **`pip list`** | Liste tous les paquets installés dans l'environnement | `pip list` |
| **`pip show <pkg>`** | Affiche les détails d'un paquet (version, emplacement, dépendances) | `pip show requests` |
| **`pip freeze`** | Affiche les paquets installés au format `nom==version` (idéal pour les fichiers d'exigences) | `pip freeze > requirements.txt` |
| **`pip search <term>`** | *Désactivé sur PyPI*. Préférer la recherche directe sur [pypi.org](https://pypi.org?utm_source=gemini) | N/A |
| **`pip check`** | Vérifie si les dépendances installées sont compatibles entre elles | `pip check` |
| **`pip cache purge`** | Vide le cache local des roues (*wheels*) et archives téléchargées | `pip cache purge` |

> 💡 **Bonne pratique :** Exécutez toujours `pip` au travers de `python -m pip` pour vous assurer d'installer les paquets dans l'environnement Python actif (venv).

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

#exécuter une commande shell - lancer mspaint
os.system("mspaint")
```

> 💡 **Bonne pratique :** Privilégiez l'utilisation de `pathlib.Path` plutôt que `os.path` pour une gestion interplateforme plus claire et élégante des chemins.

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

## Exemple de synthèse

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

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script Python qui crée un dossier nommé `export`, y génère un fichier texte `notes.txt` contenant trois lignes de votre choix, puis affiche la taille du fichier à l'écran.

**Exercice 2 :** Créez une fonction qui accepte le chemin d'un répertoire en paramètre, liste tous les fichiers `.py` présents dans ce dossier, puis génère une archive `modules.zip` les regroupant tous.
