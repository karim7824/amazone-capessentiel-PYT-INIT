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


## Créer un fichier text en unicode - ouvrir, ecrire, lire

La création d'un fichier texte en encodage Unicode garantit la prise en charge universelle des caractères accentués et des symboles internationaux. Les fonctions natives permettent d'ouvrir, d'écrire et de lire ces contenus en toute sécurité.

```python

# Création, écriture et lecture d'un fichier texte en UTF-8
with open("document.txt", "w", encoding="utf-8") as f:
    f.write("Texte en Unicode avec des accents : é, à, ê.")

with open("document.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

```

> 💡 Spécifiez systématiquement l'argument `encoding="utf-8"` lors de l'ouverture de fichiers texte pour éviter les erreurs de décodage selon les systèmes d'exploitation.

---

### Exemple de synthèse

```python
# Programme complet combinant les concepts de streams et la gestion de fichiers Unicode

nom_fichier = "message_unicode.txt"

# 1. Écriture dans un fichier texte en Unicode
with open(nom_fichier, "w", encoding="utf-8") as fichier_sortie:
    fichier_sortie.write("Bonjour Karim !\n")
    fichier_sortie.write("Apprentissage de la gestion des flux et fichiers en Python.\n")

# 2. Lecture du fichier texte via un flux sécurisé
with open(nom_fichier, "r", encoding="utf-8") as fichier_entree:
    for numero_ligne, ligne in enumerate(fichier_entree, start=1):
        print(f"Ligne {numero_ligne} : {ligne.strip()}")

```

### Exercices de fin de chapitre

1. **Exercice 1 :** Écrivez un script qui crée un fichier texte nommé `notes.txt` en encodage Unicode, puis y inscrit une phrase comportant des caractères accentués.
2. **Exercice 2 :** Ouvrez le fichier `notes.txt` en mode lecture avec l'encodage approprié, lisez son contenu global et affichez-le dans la console.
