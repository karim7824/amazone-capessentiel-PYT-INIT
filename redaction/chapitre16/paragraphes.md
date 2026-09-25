# Chapitre 16 : Gestion des fichiers et des répertoires

La gestion des fichiers et des répertoires permet d'interagir directement avec le système de stockage pour enregistrer et restituer des informations. Maîtriser ces concepts est indispensable pour persister l'état de vos applications.
Dans ce chapitre :

* Concepts généraux sur les streams et fichiers
* Créer un fichier texte en unicode : ouverture, écriture et lecture

---

## Concepts généraux sur fichiers

La manipulation de fichiers en Python repose principalement sur l'ouverture de flux via la fonction intégrée open(), qui prend en charge deux types fondamentaux de formats :

**Les fichiers texte** : contenant des caractères encodés (généralement en UTF-8) lisibles par un humain. Chaque ligne s'y termine par un caractère de saut de ligne (\n).

**Les fichiers binaires** : stockant des données brutes sous forme d'octets (images, exécutables, fichiers audio). Leur ouverture nécessite d'ajouter le suffixe b aux modes de lecture ou d'écriture (par exemple 'rb' ou 'wb').

**Accès séquentiel (fichier texte)**
with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())

**Accès aléatoire (fichier binaire) avec seek()**
with open("data.bin", "rb") as f:
    f.seek(10)          # Se déplace au 10ème octet
    octet = f.read(1)    # Lit 1 octet à cet endroit précis
    print(f.tell())     # Affiche la position actuelle (11)


---
## Lecture d'un fichier text en unicode 

Les méthodes de lecture

| Méthode | Ce qu'elle lit | Type retourné | Utilisation idéale |
| --- | --- | --- | --- |
| **`read()`** | L'intégralité du fichier d'un seul coup. | `str` | Fichiers de petite taille dont on veut tout le contenu. |
| **`read(1)`** | Exactement **1 caractère** Unicode (et non 1 octet). | `str` | Analyse caractère par caractère (parsing précis, machines à états). |
| **`readline()`** | Une seule ligne à la fois (jusqu'au `\n` inclus). | `str` | Traitement ligne par ligne sans charger tout le fichier en mémoire. |
| **`readlines()`** | Toutes les lignes du fichier sous forme de liste. | `list[str]` | Petit fichier dont on veut manipuler les lignes individuellement via des index. |

**`read()` et `read(1)` — Lecture par caractères**

* **`f.read()`** lit tout le contenu d'un coup.
* **`f.read(n)`** lit $n$ **caractères** Unicode. Si l'on écrit `read(1)`, Python extrait 1 caractère complet, peu importe le nombre d'octets codants en UTF-8.

```python
with open("texte_unicode.txt", "r", encoding="utf-8") as f:
    premier_caractere = f.read(1)  # Lit 'É' ou '🐍' (1 caractère Unicode)
    reste_du_texte = f.read()       # Lit tout le reste

```

**`readline()` — Lecture ligne par ligne**

Lit la ligne suivante jusqu'au caractère de fin de ligne `\n`. Renvoie une chaîne vide `""` lorsque la fin du fichier (EOF) est atteinte.

```python
with open("texte_unicode.txt", "r", encoding="utf-8") as f:
    ligne = f.readline()
    while ligne != "":
        print(ligne.strip())  # strip() retire le \n final
        ligne = f.readline()

```

**`readlines()` — Liste de toutes les lignes**

Charge tout le fichier en mémoire et découpe le contenu en une liste de chaînes de caractères.

```python
with open("texte_unicode.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()  # ["Première ligne\n", "Deuxième ligne\n", ...]
    print(f"Nombre de lignes : {len(lignes)}")

```

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

## Recherche dans un répertoire

| Méthode | Usage | Récursif ? | Support de motifs (`*.py`) |
| --- | --- | --- | --- |
| **`Path.glob("*.py")`** | Fichiers `.py` dans le dossier courant uniquement | Non | Oui |
| **`Path.rglob("*.py")`** | Fichiers `.py` dans le dossier et **tous ses sous-dossiers** | Oui | Oui |
| **`Path.walk()`** *(3.12+)* | Générateur arborescent complet (style `os.walk`) | Oui | Non (filtrage manuel) |

Recherche des fichiers *.py dans un répertoire de manière récursive
```python
from pathlib import Path

# Parcours récursif de tous les fichiers .py à partir du dossier courant
for fichier in Path(".").rglob("*.py"):
    print(fichier)

Recherche des fichiers *.py dans un répertoire 
```python
from pathlib import Path

# Parcours récursif de tous les fichiers .py à partir du dossier courant
for fichier in Path(".").rglob("*.py"):
    print(fichier)

```
Si vous utilisez `Path.walk()`, le filtrage doit se faire manuellement dans la boucle à l'aide de `.match()` ou `.endswith()` :
```python
from pathlib import Path

# Path.walk() génère des tuples (racine, dossiers, fichiers)
for root, dirs, files in Path(".").walk():
    for file in files:
        if file.endswith(".py"):  # ou Path(file).match("*.py")
            chemin_complet = root / file
            print(chemin_complet)

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

## Exemple de synthèse

```python
# Programme complet combinant les concepts de streams et la gestion de fichiers Unicode

nom_fichier = "message_unicode.txt"

# Écriture dans un fichier texte en Unicode
with open(nom_fichier, "w", encoding="utf-8") as fichier_sortie:
    fichier_sortie.write("Bonjour Karim !\n")
    fichier_sortie.write("Apprentissage de la gestion des flux et fichiers en Python.\n")

# Lecture du fichier texte via un flux sécurisé
with open(nom_fichier, "r", encoding="utf-8") as fichier_entree:
    for numero_ligne, ligne in enumerate(fichier_entree, start=1):
        print(f"Ligne {numero_ligne} : {ligne.strip()}")

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script qui crée un fichier texte nommé `notes.txt` en encodage Unicode, puis y inscrit une phrase comportant des caractères accentués.

**Exercice 2 :** Ouvrez le fichier `notes.txt` en mode lecture avec l'encodage approprié, lisez son contenu global et affichez-le dans la console.
