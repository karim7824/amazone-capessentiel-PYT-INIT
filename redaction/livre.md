# Chapitre 1 : Présentation du langage Python

Ce chapitre vous présente l'origine, les caractéristiques fondamentales et le fonctionnement du langage Python. Vous comprendrez son architecture, son écosystème d'implémentations ainsi que ses domaines d'application privilégiés. Cette vue d'ensemble vous permettra d'appréhender sereinement les choix techniques liés à l'adoption de Python dans vos projets.

Dans ce chapitre :

* Historique
* Caractéristiques du langage - compilé ou interprété
* Lien entre Python et le langage C
* Rôles de Cython, IronPython et Jython
* Popularité de Python par rapport aux autres langages
* Types d'applications pour Python

## Historique

Créé par Guido van Rossum et publié en 1991, Python a été conçu avec pour objectif prioritaire la lisibilité du code. Son nom provient de la troupe comique britannique *Monty Python*. Le langage a évolué à travers deux versions majeures incontournables : Python 2 (désormais obsolète) et Python 3, la norme standard actuelle.

```python
# Vérifier la version exacte de Python exécutée par le système
import sys

print("Version de Python utilisée :")
print(sys.version)

```

> 💡 **Bonne pratique :** Utilisez exclusivement Python 3.x pour tout nouveau projet, car Python 2 n'est plus maintenu depuis le 1er janvier 2020.

## Caractéristiques du langage - compilé ou interprété

Python est un langage interprété et à typage dynamique. Le code source `.py` est d'abord transformé en bytecode `.pyc`, puis exécuté par la machine virtuelle Python (PVM). Cette architecture permet d'exécuter un même script sur tout système d'exploitation sans modification du code.

```python
# Exemple de script Python interprété à typage dynamique
message = "Bonjour tout le monde"  # Type string attribué automatiquement
print(type(message))

message = 42                       # Le type devient un entier sans erreur
print(type(message))

```

> 💡 **À retenir :** Le typage dynamique apporte une grande flexibilité de développement, mais exige des tests rigoureux pour éviter les erreurs de type à l'exécution.

## Lien entre Python et le langage C

L'implémentation de référence de Python est CPython, écrite entièrement en langage C. CPython transforme le code source Python en instructions bas niveau exécutables directement par le processeur via le langage C. Ce lien étroit permet à Python d'interagir facilement avec des bibliothèques C système très rapides.

```python
# Démonstration de l'utilisation d'une fonction C sous-jacente via la bibliothèque standard
import math

# La fonction math.sqrt fait appel aux instructions C optimisées
resultat = math.sqrt(144)
print("Racine carrée calculée via CPython :", resultat)

```

** Workflow : Cycle de conversion Python $\rightarrow$ `.so` / `.dll` via Cython **

```
 [1. Code Python (.py)] 
         │
         ▼
 [2. Optimisation (.pyx)] ── (Optionnel : ajout de types C)
         │
         ▼
 [3. Cythonisation] ───────► Génère le fichier C intermediary (.c)
         │
         ▼
 [4. Compilation C] ────────► Compilateur natif (GCC / Clang / MSVC)
         │
         ▼
 [5. Binaire final] ────────► Extension native (.so / .pyd / .dll)

```

> 💡 **Piège classique :** La présence du verrou global du fermenteur (GIL) dans CPython limite le véritable multithreading parallèle sur les processeurs multi-cœurs.

## Rôles de Cython, IronPython et Jython

Cython permet de compiler du code Python en extensions C pour obtenir des performances proches du langage C. IronPython permet d'exécuter du code Python sur l'écosystème Microsoft .NET, tandis que Jython compile le code Python en bytecode Java pour la JVM. Ces déclinaisons facilitent l'intégration de Python dans des environnements d'entreprise spécifiques.

```python
# Exemple de logique métier en Python standard, convertible via Cython pour optimisation
def calculer_somme(limite: int) -> int:
    total = 0
    for i in range(limite):
        total += i
    return total

print("Résultat du calcul :", calculer_somme(100000))

```

> 💡 **Note :** Privilégiez toujours CPython standard sauf si vous avez une contrainte stricte d'intégration avec .NET (IronPython) ou Java (Jython).

## Popularité de Python par rapport aux autres langages

Python se classe régulièrement parmi les langages les plus populaires aux index TIOBE et GitHub. Cette popularité s'explique par sa syntaxe claire et intuitive qui accélère la vitesse de développement. Sa vaste communauté garantit un écosystème de bibliothèques très riche pour résoudre presque tout problème informatique.

```python
# Exemple illustrant la concision de la syntaxe Python face à d'autres langages
langages = ["Python", "Java", "C++", "C#"]

# Filtrage et mise en majuscules en une seule ligne (list comprehension)
populaires = [lang.upper() for lang in langages if lang == "Python"]
print("Langage sélectionné :", populaires)

```

> 💡 **Bonne pratique :** Profitez du grand nombre de paquets officiels hébergés sur PyPI (Python Package Index) pour éviter de réinventer la roue.


Panorama résumant la popularité comparative de ces 5 langages (selon les indices **TIOBE** et **PYPL**) :

| Langage | Rang TIOBE | Part PYPL (Tutoriels) | Tendances & Usages principaux |
| --- | --- | --- | --- |
| **Python** | **#1** (~21 %) | **#1** (~36 %) | **Dominant** (IA, Data, Web, Automatisation) |
| **C++** | **#3** (~8 %) | **#2** (~13 %)* | **Très stable** (Jeux vidéo, Système, Embarqué) |
| **Java** | **#4** (~8 %) | **#3** (~10 %) | **Solide** (Backend Entreprise, Android historique) |
| **C#** | **#5** (~7 %) | **#7** (~3 %) | **En hausse** (Écosystème .NET, Jeux/Unity, Cloud) |
| **PHP** | **#18** (~1,2 %) | **#9** (~3 %) | **En déclin léger** (Web CMS/Symfony, marché très axé sur la maintenance) |

**Note : L'indice PYPL regroupe les recherches C et C++ dans la même catégorie.*

## Types d'applications pour Python

Python s'impose comme le langage leader en intelligence artificielle, science des données et apprentissage automatique. Il est également très utilisé dans le développement web backend avec des frameworks comme Django et FastAPI. Enfin, il excelle dans l'automatisation de tâches système, le scripting d'infrastructure et l'ingénierie de données.

```python
# Exemple d'automatisation système : création et écriture rapide dans un fichier journal
with open("systeme.log", "w", encoding="utf-8") as fichier:
    fichier.write("INFO: Démarrage de l'application réussi.\n")

# Lecture du fichier journal généré
with open("systeme.log", "r", encoding="utf-8") as fichier:
    print("Contenu du journal :", fichier.read().strip())

# Surveillance de l'activité système
Python
import time
import psutil

def surveiller_systeme():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disque = psutil.disk_usage('/').percent
    print(f"[MONITORING] CPU: {cpu}% | RAM: {ram}% | Disque: {disque}%")

if __name__ == "__main__":
    while True:
        surveiller_systeme()
        time.sleep(2)

```

| Domaine / Type d'application | Cas d'usage principaux | Frameworks & Bibliothèques clés |
| --- | --- | --- |
| **Développement Web (Backend)** | API REST/GraphQL, plateformes web, CMS, microservices | Django, FastAPI, Flask |
| **Data Science & Big Data** | Analyse de données, statistiques, manipulation de jeux de données complexes | Pandas, NumPy, Polars |
| **Intelligence Artificielle & ML** | Apprentissage automatique, Deep Learning, vision par ordinateur, LLM | PyTorch, TensorFlow, Scikit-Learn, OpenCV, LangChain |
| **Automation & Scripting** | Automatisation de tâches système, web scraping, scripts d'administration / DevOps | Ansible, BeautifulSoup, Scrapy, Selenium |
| **Supervision & Systèmes** | Outillage réseau, collecte de métriques système, agents de monitoring | `psutil`, Glances, Fabric |
| **Interfaces Graphiques (GUI Desktop)** | Applications de bureau multi-plateformes | PyQt / PySide, Tkinter, CustomTkinter, Flet (Flutter) |
| **Tests & Qualité Logicielle** | Tests unitaires, tests d'intégration, automatisation QA | Pytest, Robot Framework, Unittest |
| **Calcul Scientifique & Financier** | Simulation physique, modélisation mathématique, quant trading | SciPy, SymPy, QuantLib |
| **Jeux Vidéo & Multimédia** | Prototypage de jeux 2D, scripts logiques pour moteurs 3D | Pygame, Arcade, Godot (via GDNative/Python) |

---

### Exemple de synthèse

Cet exemple regroupe la vérification de l'environnement, le typage dynamique et le traitement de données simple dans un script unique :

```python
import sys
import platform

# 1. Collecte d'informations environnementales
infos_systeme = {
    "version_python": sys.version.split()[0],
    "os": platform.system(),
    "statut": "Opérationnel"
}

# 2. Traitement et affichage
print("--- Bilan de l'environnement Python ---")
for cle, valeur in infos_systeme.items():
    print(f"{cle.capitalize()} : {valeur}")

# 3. Écriture d'un rapport de synthèse
with open("rapport_intro.txt", "w", encoding="utf-8") as f:
    f.write(f"Rapport généré sous {infos_systeme['os']} avec Python {infos_systeme['version_python']}\n")

print("Rapport écrit avec succès dans 'rapport_intro.txt'.")

```

---

### Exercices de fin de chapitre

1.  **Exercice 1 : Inspection de l'environnement d'exécution**
Écrivez une instruction qui permet d'afficher la version de Python
Écrivez une instruction qui permet d'afficher la variable d'environnement PATH
Écrivez une instruction qui permet de lancer une commande shell 

2. **Exercice 2 : une instruction de boucle**
Écrivez une instruction de boucle qui compte de 1 à 10 et afficher 'O' 'OO' 'OOO' allant de 1 à 10 en utilisant range()


# Chapitre 2 : Installation de l'environnement de programmation Python

Ce chapitre vous guide dans la mise en place d'un environnement de développement Python complet, propre et opérationnel. Vous apprendrez à installer l'interpréteur officiel, à exécuter vos premiers scripts et à utiliser le mode interactif. Enfin, vous découvrirez comment isoler vos projets grâce aux environnements virtuels, une bonne pratique incontournable en entreprise.

Dans ce chapitre :

* Installation de base de l'interpréteur x64
* Création d'un projet Python main.py avec la condition `__name__ == '__main__'`
* Lancement de scripts et utilisation de Python en mode REPL
* Mise en place d'un environnement virtuel avec `venv`

## Installation de base de l'interpréteur x64

L'installation de Python s'effectue en téléchargeant l'exécutable officiel 64-bit depuis le site [python.org/downloads](https://www.python.org/downloads/). Sous Windows, il est essentiel de cocher l'option "Add python.exe to PATH" lors de l'installation pour pouvoir exécuter Python depuis n'importe quel terminal. Sous Linux et macOS, Python 3 est généralement préinstallé ou accessible via le gestionnaire de paquets du système.

```python
import platform

architecture = platform.architecture()[0]
print(f"Architecture : {architecture}")
# Affiche directement : "64bit" ou "32bit"
```

**Différence entre `python`, `python3` et `py`**

| Commande | Environnement | Description |
| --- | --- | --- |
| **`python`** | Multiplateforme | Lance l'interpréteur par défaut configuré dans le `PATH`. |
| **`python3`** | Linux / macOS | Commande standard pour garantir l'exécution de **Python 3**. |
| **`py`** | Windows uniquement | Launcher qui détecte et exécute la bonne version (x64/x86) sans paramétrer le `PATH`. |
---

**Vérifier l'installation et l'architecture (64-bit)**
```bash
python --version
# Ou sous Windows via le launcher :
py -V
```

**Exécuter un fichier script (.py)**
```bash
python mon_script.py
python3 mon_script.py
py mon_script.py
```

> 💡 **Bonne pratique :** Vérifiez toujours après l'installation que la commande `python --version` (ou `python3 --version`) répond correctement dans votre invite de commande.

## Créer module Python main.py avec la condition `__name__ == '__main__'`

En Python, la condition `if __name__ == '__main__':` permet de définir le point d'entrée principal d'un script. Elle garantit que le bloc de code sous-jacent ne s'exécute que lorsque le fichier est lancé directement, et non lorsqu'il est importé comme module dans un autre fichier. C'est une structure standard pour organiser proprement vos projets.

```python
# Fichier : main.py

def afficher_message(nom: str) -> None:
    print(f"Bonjour à tous, bienvenue dans le projet {nom} !")

if __name__ == "__main__":
    # Ce bloc s'exécute uniquement si main.py est le fichier principal
    afficher_message("Python 3")

```

> 💡 **À retenir :** Intégrez systématiquement cette condition dans vos scripts principaux pour rendre votre code réutilisable et modulaire.

## Lancement de lab_main.py

L'exécution d'un script Python s'effectue depuis le terminal à l'aide de l'interpréteur `python` suivi du nom du fichier. Vous pouvez rediriger ou manipuler les arguments de la ligne de commande directement au sein du script grâce au module standard `sys`. Cela permet de créer des outils d'automatisation et de traitement par lots flexibles.

```python
# Fichier : lab_main.py
import sys

print("Lancement du laboratoire Python...")
print("Arguments passés au script :", sys.argv)

```

> 💡 **Bonne pratique :** Lancez vos scripts depuis le dossier racine de votre projet pour éviter les erreurs de chemins relatifs lors de l'ouverture de fichiers.

## Utilisation de Python en mode REPL

Le mode REPL (*Read-Eval-Print Loop*) est la console interactive de Python, accessible en tapant simplement `python` dans votre terminal. Il permet de tester immédiatement des expressions, des syntaxes ou de courtes fonctions sans avoir à créer un fichier de code sur le disque. C'est un outil formidable pour l'expérimentation et le débogage rapide.

```python
# Simulation d'une session REPL interactive
# >>> a = 10
# >>> b = 20
# >>> a + b
30
# >>> type(a + b)
<class 'int'>

```

> 💡 **Note :** Pour quitter le mode REPL dans votre terminal, tapez la fonction `exit()` ou utilisez le raccourci `Ctrl + Z` (Windows) ou `Ctrl + D` (Linux/macOS).

## Mettre en place un environnement virtuel pour une version de Python - venv

Un environnement virtuel permet d'isoler les dépendances et bibliothèques de chaque projet dans un dossier dédié, évitant ainsi les conflits de versions entre vos différents projets. Le module officiel `venv` est inclus de base avec Python et permet de créer ces espaces isolés en une seule commande.

```bash
# Commandes terminal pour créer et activer un environnement virtuel
python -m venv .venv

# Sous Windows (PowerShell) :
# .venv\Scripts\Activate.ps1

# Sous Linux/macOS :
# source .venv/bin/activate

```

```python
# Code Python permettant de vérifier si le script s'exécute dans un environnement virtuel
import sys

dans_venv = sys.prefix != sys.base_prefix
print("Exécution dans un environnement virtuel :", dans_venv)

```

> 💡 **Bonne pratique :** N'ajoutez jamais le dossier `.venv` à votre gestionnaire de version (Git) ; ajoutez-le toujours dans votre fichier `.gitignore`.

---

## Envrionnements de développement (IDE=Integrated Development Environment ou Environnement de Développement Intégré)

Logiciels uniques qui regroupe tous les outils nécessaires au développement de code : un éditeur de texte, un compilateur/interpréteur, des outils d'automatisation et un débogueur. Les fonctionnalités des IDEs sont extensibles (plugins)

**Les principaux IDE et Éditeurs pour Python**

| Outil | Éditeur / Type | Points forts | Cas d'usage idéal |
| --- | --- | --- | --- |
| **VS Code** | Éditeur extensible | Ultra-léger, écosystème d'extensions gigantesque, support multi-langages | Polyvalent (Web, Scripting, Data) |
| **PyCharm** | IDE complet (JetBrains) | Autocomplétion intelligente, refactoring puissant, gestion venv/Git intégrée | Projets Python complexes / Django |
| **Jupyter Notebook / Lab** | Environnement interactif | Exécution cellule par cellule, visualisation de données en direct | Data Science, Machine Learning, R&D |
| **Spyder** | IDE scientifique | Proche de MATLAB, explorateur de variables et de graphiques intégré | Calcul scientifique / Analyse de données |
| **IDLE** | IDE minimaliste | Fourni par défaut avec l'installation officielle de Python | Apprentissage / Débutants |



## Exemple de synthèse

Cet exemple combine la vérification du point d'entrée principal, la détection de l'environnement virtuel et la création automatique d'un script de laboratoire prêts à l'emploi :

```python
import sys
import os

def verifier_environnement() -> dict:
    return {
        "executable": sys.executable,
        "est_virtuel": sys.prefix != sys.base_prefix,
        "dossier_travail": os.getcwd()
    }

def creer_script_laboratoire(nom_fichier: str) -> None:
    contenu = (
        "# Script de laboratoire généré automatiquement\n"
        "import sys\n\n"
        "if __name__ == '__main__':\n"
        "    print('Laboratoire opérationnel !')\n"
    )
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(contenu)

if __name__ == "__main__":
    print("--- Diagnostic du projet ---")
    info = verifier_environnement()
    print(f"Interpréteur : {info['executable']}")
    print(f"Environnement virtuel actif : {info['est_virtuel']}")
    
    script_lab = "lab_main.py"
    creer_script_laboratoire(script_lab)
    print(f"Fichier '{script_lab}' généré avec succès.")

```

---

## Exercices de fin de chapitre

**Exercice 1 : Création et exécution d'un script structuré**
Créez un fichier nommé `main.py` qui définit une fonction `saluer(nom)`. Dans le bloc principal `if __name__ == '__main__':`, appelez cette fonction avec votre prénom, puis faites en sorte que le programme écrive le message de salutation dans un fichier texte nommé `bienvenue.txt`.

**Exercice 2 : Générateur d'environnement et vérification venv**
Écrivez un script Python nommé `check_env.py` qui teste si le programme est exécuté au sein d'un environnement virtuel `venv`. Si ce n'est pas le cas, le script doit afficher un avertissement recommandant d'activer un environnement virtuel. Si l'environnement virtuel est actif, le script doit inscrire le chemin de l'interpréteur dans un fichier `env_status.log`.


# Chapitre 3 : Définir et manipuler des données types en mémoire

Maîtriser les types de données et leur manipulation en mémoire est essentiel pour stocker et traiter efficacement l'information. Ces concepts fondamentaux garantissent la rigueur et la logique de vos programmes en Python.
Dans ce chapitre :

* Déclaration et affectation de variables
* Types scalaires (int, float, bool, str)
* Types agrégés (list, tuple, dict, set)
* Valeurs littérales et portée des variables (locale, globale)

---

## Déclaration de variables

Une variable en Python : une étiquette mémoire. Une **variable** est un nom qui pointe vers un emplacement mémoire contenant une donnée.

En Python, la création se fait par simple **affectation** avec le signe `=` :

```python
age = 25  # L'objet 25 est stocké en mémoire, 'age' pointe dessus.

```

* **Typage dynamique :** Inutile de déclarer le type à l'avance (`int`, `str`, etc.). L'interpréteur le déduit automatiquement lors de l'exécution.
* **Mécanisme :** Contrairement à d'autres langages où la variable est une « boîte » qui contient la valeur, Python fonctionne par étiquettes : le nom pointe vers l'objet créé en mémoire.

---

### Normes de nommage (PEP 8)

| Règle | Convention | Exemples |
| --- | --- | --- |
| **Style principal** | **`snake_case`** (minuscules + tirets bas) | `nom_utilisateur`, `prix_ttc` |
| **Lisibilité** | Des noms explicites et descriptifs | `total_commandes` (éviter `x` ou `t`) |
| **Composition** | Lettres, chiffres et `_` uniquement | `user_1` (interdit de commencer par un chiffre : `1user`) |
| **Sensibilité** | Respect de la casse (majuscules/minuscules) | `age` et `Age` sont deux variables distinctes |
| **Mots réservés** | Interdiction d'utiliser les mots-clés Python | Éviter `class`, `def`, `if`, `import`, etc. |

> 💡 Le nom d'une variable doit commencer par une lettre ou un tiret bas (`_`) et ne peut pas utiliser un mot-clé réservé du langage (comme `if`, `def`, `class`).

---

## Types de données scalaires - int, float, bool, str

Les types scalaires représentent des valeurs uniques et atomiques, non décomposables en sous-éléments. Ils constituent la base de toute manipulation numérique, textuelle ou logique.

Voici le tableau corrigé, sans les balises `<br>` superflues ni les sauts de ligne intempestifs qui cassaient le rendu Markdown :

Voici le tableau propre, une ligne par type pour éviter le bazar des balises HTML :

| Catégorie | Type (`type()`) | Mutabilité | Exemples de syntaxe |
| --- | --- | --- | --- |
| **Numérique** | `int` (entier) | Immuable | `10`, `-5` |
| **Numérique** | `float` (décimal) | Immuable | `3.14`, `2.0` |
| **Numérique** | `complex` (complexe) | Immuable | `1 + 2j` |
| **Texte** | `str` (chaîne) | Immuable | `"Bonjour"`, `'Python'` |

```python
>>># avec typage float # Flottant (float) pour les décimaux
>>> température:float =11.11
>>> type(température)
<class 'float'>
>>># typage implicite
>>> température =22.22
>>> type(température)
<class 'float'>

# avec type bool : # Booléen (bool) valant True ou False
>>> est_valide:bool = True
>>> type(est_valide)
<class 'bool'>
```

```python 
>>> a=10
>>> type(a)
<class 'int'>
>>># afficher l'adresse de la variable en mémoire (pas essentiel)
>>> hex(id(a))
'0x7ffc5b823ad8'
```

> 💡 Utilisez toujours des noms explicites pour vos variables scalaires afin d'améliorer la lisibilité immédiate du code par l'équipe projet.

---

## Types de données aggrégés - list, tuple, dict, set

Les types agrégés permettent de regrouper plusieurs valeurs au sein d'une seule structure de données en mémoire. Leur choix dépend de la nécessité d'ordre, d'unicité des éléments, ainsi que de leur mutabilité — c'est-à-dire la possibilité de modifier ou non le contenu de la structure directement en mémoire après sa création.

| Catégorie | Type (`type()`) | Mutabilité | Exemples de syntaxe |
| --- | --- | --- | --- |
| **Séquence** | `list` (liste) | **Mutable** | `[1, "dev", 3.14]` |
| **Séquence** | `tuple` (uplet) | Immuable | `(10, 20, 30)` |
| **Séquence** | `range` (séquence d'entiers) | Immuable | `range(0, 10)` |
| **Ensemble** | `set` (ensemble unique) | **Mutable** | `{1, 2, 3}` |
| **Mapping** | `dict` (dictionnaire) | **Mutable** | `{"nom": "Karim", "age": 40}` |
| **Spécial** | `NoneType` | Immuable | `None` |


**La Liste (`list`) — `utilisateurs = ["Alice", "Bob", "Charlie"]`**

La liste est **ordered** (ordonnée) et **mutable** (modifiable sur place).

```python
utilisateurs = ["Alice", "Bob", "Charlie"]

# --- Ajout d'éléments ---
utilisateurs.append("David")          # Ajoute à la fin -> ["Alice", "Bob", "Charlie", "David"]
utilisateurs.insert(1, "Eve")          # Insère à l'index 1 -> ["Alice", "Eve", "Bob", "Charlie", "David"]

# --- Suppression d'éléments ---
utilisateurs.remove("Bob")             # Supprime la première occurrence de "Bob"
dernier = utilisateurs.pop()          # Retire et renvoie le dernier élément ("David")
del utilisateurs[0]                    # Supprime l'élément à l'index 0 ("Alice")

# --- Modification et accès ---
utilisateurs[0] = "Éléonore"           # Modifie l'élément en position 0
premier = utilisateurs[0]              # Accès par index

# --- Recherche et tri ---
existe = "Charlie" in utilisateurs     # Renvoie True ou False
utilisateurs.sort()                    # Trie la liste par ordre alphabétique en place

```

---

**Le Tuple (`tuple`) — `coordonnees = (10.0, 20.0)`**

Le tuple est **ordered** (ordonné) mais **immuable** (impossible à modifier directement après création).

```python
coordonnees = (10.0, 20.0)

# --- Accès et découpage (Slicing) ---
x = coordonnees[0]                     # Extrait la latitude (10.0)
y = coordonnees[1]                     # Extrait la longitude (20.0)

# --- Unpacking (Désassemblage direct) ---
latitude, longitude = coordonnees       # Assigne 10.0 à latitude et 20.0 à longitude

# --- "Modification" par recréation ---
# On ne peut pas modifier un tuple, mais on peut en récréer un nouveau :
coordonnees_3d = coordonnees + (30.0,)  # Fusionne deux tuples -> (10.0, 20.0, 30.0)

# --- Méthodes de comptage ---
coordonnees.count(10.0)                # Nombre d'occurrences de 10.0 (renvoie 1)
coordonnees.index(20.0)                # Position de la valeur 20.0 (renvoie 1)

```
---

**Le Dictionnaire (`dict`) — `personne = {"nom": "Karim", "age": "20"}`**

Le dictionnaire est une structure **clé/valeur**, **mutable** et **indexée par clés unique**.

```python
personne = {"nom": "Karim", "age": "20"}

# --- Ajout et modification ---
personne["age"] = "21"                 # Modifie la valeur associée à la clé "age"
personne["ville"] = "Paris"             # Ajoute la clé "ville" si elle n'existe pas encore

# --- Accès sécurisé ---
nom = personne.get("nom")               # Renvoie "Karim"
statut = personne.get("statut", "N/A")  # Renvoie "N/A" au lieu de lever une KeyError

# --- Suppression ---
del personne["ville"]                   # Supprime la clé "ville"
age = personne.pop("age")              # Supprime "age" et renvoie sa valeur ("21")

# --- Inspection et itération ---
cles = personne.keys()                 # Renvoie dict_keys(["nom"])
valeurs = personne.values()             # Renvoie dict_values(["Karim"])

# Parcourir les paires clé/valeur :
for cle, valeur in personne.items():
    print(f"{cle} : {valeur}")

```

> 💡 Privilégiez les tuples pour des données fixes qui ne doivent pas être altérées au cours de l'exécution du programme, garantissant ainsi l'intégrité des structures.

---

## Valeurs littérales

Une valeur littérale correspond à la représentation directe d'une donnée constante inscrite textuellement dans le code source du programme. Elle permet d'assigner des valeurs figées sans calcul préalable.


**Littéraux Numériques**

```python
# --- Entiers (int) ---
seuil_maximal = 100         # Décimal standard
octets = 0b1010             # Binaire (commence par 0b -> vaut 10)
hexadecimal = 0xFF          # Hexadécimal (commence par 0x -> vaut 255)
octal = 0o77                # Octal (commence par 0o -> vaut 63)
grand_nombre = 1_000_000    # Les underscores améliorent la lisibilité (vaut 1000000)

# --- Décimaux (float) ---
taux_tva = 20.0             # Notation décimale classique
pi_approx = 3.14159         # Flottant standard
charge_electron = 1.6e-19   # Notation scientifique (1.6 x 10^-19)

# --- Complexes (complex) ---
impedance = 3 + 4j         # Littéral complexe (partie imaginaire avec 'j' ou 'J')

```

---

**Littéraux Textuels (Chaînes de caractères - `str`)**

```python
# --- Apostrophes et Guillemets ---
message_erreur = "Erreur 404"  # Guillemets doubles
nom_utilisateur = 'Alice'       # Apostrophes simples

# --- Caractères d'échappement ---
chemin_windows = "C:\\Python\\scripts"  # Échappement de l'antislash avec \\
citation = "Il a dit : \"Bonjour !\""   # Échappement des guillemets avec \"
saut_de_ligne = "Ligne 1\nLigne 2"      # \n pour le saut de ligne

# --- Raw Strings (Chaînes brutes) ---
# Le préfixe 'r' désactive l'interprétation des caractères d'échappement
regex_pattern = r"C:\nouvelle_dossier\test"  # Le \n n'est pas interprété comme un saut de ligne

# --- F-Strings (Formatage dynamique) ---
code = 404
f_string = f"Erreur système : {code}"   # Évalue la variable entre accolades

# --- Multi-lignes (Docstrings / Textes longs) ---
sql_query = """
SELECT id, nom 
FROM utilisateurs 
WHERE actif = True
"""

```

---

**Littéraux Booléens et Spécial**

```python
# --- Booléens (bool) ---
est_valide = True           # Première lettre obligatoirement en majuscule
est_connecte = False

# --- Littéral Spécial (NoneType) ---
valeur_inconnue = None      # Représente l'absence explicite de valeur

```

---

**Littéraux de Collections (Structures de données)**

```python
# --- Liste (list) - Modifiable ---
coordonnees = [48.8566, 2.3522]

# --- Tuple (tuple) - Immuable ---
dimensions = (1920, 1080)

# --- Dictionnaire (dict) - Clé/Valeur ---
config = {"port": 8080, "debug": True}

# --- Ensemble (set) - Valeurs uniques ---
ports_autorises = {80, 443, 8080}

```
---

## Portée de variables - globale, locale

La portée d'une variable détermine la zone du code où cette variable est accessible en lecture et en écriture. Une variable locale n'existe que dans la fonction où elle est définie, tandis qu'une variable globale est accessible dans tout le module.

```python
TAXE_GLOBALE = 0.20  # Variable globale

def calculer_total(prix_ht):
    tva = prix_ht * TAXE_GLOBALE  # 'tva' est locale à la fonction
    return prix_ht + tva

```

> 💡 Limitez au maximum l'utilisation de variables globales pour éviter les effets de bord imprévisibles et faciliter la maintenance du code.

---

## Exemple de synthèse

```python
# Programme complet combinant variables, types scalaires, agrégés et portée
TAUX_REDUCTION = 0.15  # Variable globale

def traiter_commande(client, articles_prix):
    """Calcule le montant total d'une commande avec application d'une réduction."""
    total_brut = sum(articles_prix)           # Utilisation d'un type agrégé (list)
    est_fidele = True                         # Type scalaire booléen
    
    if est_fidele:
        montant_final = total_brut * (1 - TAUX_REDUCTION)  # Variable locale
    else:
        montant_final = total_brut
        
    return f"Client : {client} | Total à payer : {montant_final}€"

# Appel de la fonction avec des valeurs littérales
print(traiter_commande("Karim", [45.0, 15.5, 30.0]))

```

## Exercices de fin de chapitre

1. **Exercice 1 : variables scalaires** Écrivez un script qui déclare quatre variables de types scalaires différents (`int`, `float`, `bool`, `str`), puis affichez le type de chacune d'elles à l'aide de la fonction `type()`.
2. **Exercice 2 : liste** Créez une liste contenant les notes d'un étudiant, écrivez une fonction qui calcule la moyenne de ces notes, et stockez le résultat dans une variable locale avant de le retourner.


# Chapitre 4 : Les opérateurs

Comprendre et utiliser les opérateurs permet d'effectuer des calculs, de comparer des valeurs et de combiner des conditions logiques en Python. Ces mécanismes fondamentaux constituent les briques de base de toute logique algorithmique.
Dans ce chapitre :

* Opérateurs d'affectation
* Opérateurs arithmétiques
* Opérateurs relationnels
* Opérateurs logiques

---

## Les opérateurs d'affectation

Les opérateurs d'affectation permettent d'attribuer une valeur à une variable en mémoire, parfois en combinant cette affectation avec une opération mathématique. Ils simplifient l'écriture des mises à jour de variables.

Les **opérateurs d'affectation** en Python, combinant l'affectation simple et les affectations augmentées 

| Opérateur | Nom | Exemple | Équivalent à | Description |
| --- | --- | --- | --- | --- |
| **`=`** | Affectation simple | `x = 5` | `x = 5` | Assigne la valeur à la variable. |
| **`+=`** | Addition et affectation | `x += 3` | `x = x + 3` | Ajoute la valeur et réaffecte. |
| **`-=`** | Soustraction et affectation | `x -= 2` | `x = x - 2` | Soustrait la valeur et réaffecte. |
| **`*=`** | Multiplication et affectation | `x *= 4` | `x = x * 4` | Multiplie et réaffecte. |
| **`/=`** | Division et affectation | `x /= 2` | `x = x / 2` | Divise (résultat `float`) et réaffecte. |
| **`//=`** | Division entière et affectation | `x //= 2` | `x = x // 2` | Divise en tronquant le décimal et réaffecte. |
| **`%=`** | Modulo et affectation | `x %= 3` | `x = x % 3` | Calcule le reste de la division et réaffecte. |
| **`**=`** | Puissance et affectation | `x **= 2` | `x = x ** 2` | Élève à la puissance et réaffecte. |
| **`&=`** | ET binaire et affectation | `x &= 3` | `x = x & 3` | Opération bitwise AND et réaffecte. |
| **`|=`** | OU binaire et affectation | `x |= 3` | `x = x | 3` | Opération bitwise OR et réaffecte. |
| **`^=`** | OU exclusif binaire | `x ^= 3` | `x = x ^ 3` | Opération bitwise XOR et réaffecte. |
| **`>>=`** | Décalage à droite | `x >>= 1` | `x = x >> 1` | Décale les bits vers la droite et réaffecte. |
| **`<<=`** | Décalage à gauche | `x <<= 1` | `x = x << 1` | Décale les bits vers la gauche et réaffecte. |
| **`:=`** | Walrus (expression d'affectation) | `if (n := len(l)) > 0:` | *N/A* | Assigne une valeur **au sein d'une expression** (Python 3.8+). |

```python
# Affectation simple et affectation augmentée
score = 10     # Affectation simple de la valeur 10
score += 5     # Équivalent à score = score + 5

```

> 💡 L'opérateur d'affectation s'évalue de droite à gauche : la valeur ou le résultat de l'expression à droite est stocké dans la variable située à gauche.

---

## Opérateurs arithmétiques

Les opérateurs arithmétiques réalisent les calculs mathématiques usuels sur des types numériques (entiers et flottants). Ils permettent de manipuler des données quantitatives au sein des programmes.

Les **opérateurs d'affectation** en Python, combinant l'affectation simple et les affectations augmentées 

| Opérateur | Nom | Exemple | Équivalent à | Description |
| --- | --- | --- | --- | --- |
| **`=`** | Affectation simple | `x = 5` | `x = 5` | Assigne la valeur à la variable. |
| **`+=`** | Addition et affectation | `x += 3` | `x = x + 3` | Ajoute la valeur et réaffecte. |
| **`-=`** | Soustraction et affectation | `x -= 2` | `x = x - 2` | Soustrait la valeur et réaffecte. |
| **`*=`** | Multiplication et affectation | `x *= 4` | `x = x * 4` | Multiplie et réaffecte. |
| **`/=`** | Division et affectation | `x /= 2` | `x = x / 2` | Divise (résultat `float`) et réaffecte. |
| **`//=`** | Division entière et affectation | `x //= 2` | `x = x // 2` | Divise en tronquant le décimal et réaffecte. |
| **`%=`** | Modulo et affectation | `x %= 3` | `x = x % 3` | Calcule le reste de la division et réaffecte. |
| **`**=`** | Puissance et affectation | `x **= 2` | `x = x ** 2` | Élève à la puissance et réaffecte. |
| **`&=`** | ET binaire et affectation | `x &= 3` | `x = x & 3` | Opération bitwise AND et réaffecte. |
| **`|=`** | OU binaire et affectation | `x |= 3` | `x = x | 3` | Opération bitwise OR et réaffecte. |
| **`^=`** | OU exclusif binaire | `x ^= 3` | `x = x ^ 3` | Opération bitwise XOR et réaffecte. |
| **`>>=`** | Décalage à droite | `x >>= 1` | `x = x >> 1` | Décale les bits vers la droite et réaffecte. |
| **`<<=`** | Décalage à gauche | `x <<= 1` | `x = x << 1` | Décale les bits vers la gauche et réaffecte. |
| **`:=`** | Walrus (expression d'affectation) | `if (n := len(l)) > 0:` | *N/A* | Assigne une valeur **au sein d'une expression** (Python 3.8+). |

```python
# Opérations arithmétiques de base
somme = 15 + 5      # Addition (vaut 20)
division = 10 / 4   # Division flottante (vaut 2.5)

```

> 💡 Utilisez l'opérateur modulo (`%`) pour obtenir le reste d'une division entière, ce qui est particulièrement utile pour tester la parité d'un nombre.

---

## Opérateurs relationnels

Les opérateurs relationnels comparent deux valeurs ou expressions et retournent systématiquement un résultat booléen (`True` ou `False`). Ils sont indispensables pour orienter l'exécution du code selon les conditions.

Les **opérateurs relationnels** (ou opérateurs de comparaison) en Python. Ils permettent de comparer deux valeurs et renvoient toujours un **booléen** (`True` ou `False`).

| Opérateur | Signification | Exemple | Résultat (`x = 10`, `y = 5`) |
| --- | --- | --- | --- |
| **`>`** | Strictement supérieur à | `x > y` | `True` |
| **`<`** | Strictement inférieur à | `x < y` | `False` |
| **`>=`** | Supérieur ou égal à | `x >= 10` | `True` |
| **`<=`** | Inférieur ou égal à | `y <= 5` | `True` |

---
```python
x = 10
y = 5

# --- 2. Comparaisons d'ordre (<, >, <=, >=) ---
print(x > y)        # True  (10 est strictement supérieur à 5)
print(x < y)        # False (10 n'est pas inférieur à 5)
print(x >= 10)      # True  (10 est supérieur ou égal à 10)
print(y <= 5)       # True  (5 est inférieur ou égal à 5)

# --- 3. Comparaisons chaînées (spécificité Python) ---
age = 25
# Vérifie si l'âge est compris entre 18 et 65 inclus :
print(18 <= age <= 65)  # True

# --- 4. Comparaison de chaînes de caractères (ordre alphabétique / ASCII) ---
print("apple" < "banana")  # True ('a' vient avant 'b')
```
**Particularités importantes en Python**

* **Comparaisons chaînées :** Python permet d'enchaîner directement les comparaisons, ce qui rend le code très lisible.
```python
age = 25
# Équivalent à : (18 <= age) and (age <= 65)
if 18 <= age <= 65:
    print("Âge valide")

```python
# Comparaisons de valeurs
age = 18
majeur = age >= 18    # Retourne True car 18 est supérieur ou égal à 18

```

> 💡 Veillez à ne pas confondre l'opérateur d'égalité (`==`) avec l'opérateur d'affectation (`=`) pour éviter des erreurs de logique.

---

## Opérateurs logiques

Les opérateurs logiques permettent de combiner plusieurs expressions booléennes pour former des conditions complexes. Ils évaluent les relations à l'aide des opérateurs fondamentaux `and`, `or` et `not`.

Les **opérateurs de comparaison**, **logiques** (`and`, `or`, `not`) et **binationaux / bitwise** (`&`, `|`, `^`, `~`, `<<`, `>>`).

### Tableau complet des opérateurs logiques, relationnels et binaire (Bitwise)

*(Pour les exemples : `x = 10` [binaire: `1010`] et `y = 5` [binaire: `0101`])*

| Catégorie | Opérateur | Description | Exemple | Résultat |
| --- | --- | --- | --- | --- |
| **Comparaison** | **`==`** | Égal à | `x == y` | `False` |
| **Comparaison** | **`!=`** | Différent de | `x != y` | `True` |
| **Comparaison** | **`>`** | Strictement supérieur à | `x > y` | `True` |
| **Comparaison** | **`<`** | Strictement inférieur à | `x < y` | `False` |
| **Comparaison** | **`>=`** | Supérieur ou égal à | `x >= 10` | `True` |
| **Comparaison** | **`<=`** | Inférieur ou égal à | `y <= 5` | `True` |
| **Logique** | **`and`** | ET logique (True si les deux conditions sont vraies) | `(x > 5) and (y < 10)` | `True` |
| **Logique** | **`or`** | OU logique (True si au moins une condition est vraie) | `(x == 5) or (y == 5)` | `True` |
| **Logique** | **`not`** | NON logique (Inverse l'état booléen) | `not(x == y)` | `True` |
| **Bitwise** | **`&`** | ET binaire (*AND*) | `x & y` *(1010 & 0101)* | `0` *(0000)* |
| **Bitwise** | **`|`** | OU binaire (*OR*) | `x | y` *(1010 | 0101)* | `15` *(1111)* |
| **Bitwise** | **`^`** | OU exclusif binaire (*XOR*) | `x ^ y` *(1010 ^ 0101)* | `15` *(1111)* |
| **Bitwise** | **`~`** | Complément à un binaire (*NOT*) | `~x` *(-(x+1))* | `-11` |
| **Bitwise** | **`<<`** | Décalage de bits à gauche | `x << 1` *(1010 -> 10100)* | `20` |
| **Bitwise** | **`>>`** | Décalage de bits à droite | `x >> 1` *(1010 -> 0101)* | `5` |


```python
x = 10
y = 5

# --- Égalité (==) et Inégalité (!=) ---
print(x == y)       # False (10 n'est pas égal à 5)
print(x != y)       # True  (10 est bien différent de 5)

# --- Comparaison de chaînes de caractères (ordre alphabétique / ASCII) ---
print("Code" == "code")    # False (sensible à la casse)
```

* **Comparaison d'identité (`is`) vs Égalité (`==`) :**
* `==` compare les **valeurs** des objets.
* `is` compare les **adresses mémoire** (si deux variables pointent vers le même objet exact).

```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True (mêmes valeurs)
print(a is b)  # False (deux objets distincts en mémoire)
```
---

## Exemple de synthèse

```python
# Programme complet combinant affectation, arithmétique, relations et logique
stock_initial = 50  # Opérateur d'affectation
ventes = 12         # Valeur littérale

# Opérateur arithmétique de soustraction combiné à l'affectation
stock_initial -= ventes  # stock_initial vaut maintenant 38

seuil_critique = 10
rupture_imminente = False

# Opérateurs relationnels et logiques
alerte_stock = (stock_initial <= seuil_critique) or rupture_imminente

print(fstock restant : {stock_initial} | Alerte active : {alerte_stock})

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script qui initialise deux variables numériques, puis utilisez les opérateurs arithmétiques pour calculer leur somme, leur produit et le reste de leur division entière.

**Exercice 2 :** Déclarez une variable représentant l'âge d'un utilisateur et une autre indiquant s'il possède une autorisation. Utilisez des opérateurs relationnels et logiques pour vérifier s'il remplit les conditions d'accès (âge supérieur ou égal à 18 et autorisation vraie).


# Chapitre 5 : Convertir les données - casting ou transtypage

La conversion de données, ou casting, permet de transformer un type de données en un autre pour assurer la compatibilité entre variables. Maîtriser ces conversions est indispensable pour traiter des entrées utilisateur ou fusionner des informations de natures différentes.
Dans ce chapitre :

* Casting et conversion de types
* Conversions implicites versus explicites

---

## Casting et conversion

Le casting consiste à transformer explicitement une valeur d'un type donné vers un autre type (par exemple d'une chaîne de caractères vers un entier). Cette opération est indispensable pour manipuler des données textuelles provenant d'interfaces ou de fichiers.

```python
# Conversion explicite d'une chaîne en entier
saisie_utilisateur = "25"
age = int(saisie_utilisateur)
```

> 💡 Assurez-vous que le contenu de la chaîne est syntaxiquement convertible avant d'appliquer une fonction de casting, sous peine de déclencher une exception de type `ValueError`.

Comment savoir si un contenu se prête à la conversion ?

| Méthode | Chiffres standard (`0-9`) | Chiffres arabes/indiens | Exposants / Indices (`²`) | Fractions (`½`) |
| --- | --- | --- | --- | --- |
| **`s.isdecimal()`** | Oui | Oui | Non | Non |
| **`s.isdigit()`** | Oui | Oui | Oui | Non |
| **`s.isnumeric()`** | Oui | Oui | Oui | Oui |

```python
code = "12121"
print(code.isdigit())  # True

# Attention aux limites :
print("-10".isdigit())   # False (le caractère '-' n'est pas un chiffre)
print("3.14".isdigit())  # False (le point '.' n'est pas un chiffre)

```
On peut se creéer une fonction qui essaie de convertir avec prudence un contenu 

```python
def try_cast_int(valeur, defaut=None):
    try:
        return int(valeur)
    except (ValueError, TypeError):
        return defaut

# Utilisation
print(try_cast_int("12121"))   # 12121 (int)
print(try_cast_int("-5"))      # -5 (int)
print(try_cast_int("abc"))     # None
print(try_cast_int("abc", 0))  # 0

```


---

## Conversions implicites vs explicites

Python réalise parfois des conversions implicites automatiques sans intervention du développeur pour éviter les pertes de données, tandis que les conversions explicites exigent l'appel direct à des fonctions dédiées comme `int()`, `float()` ou `str()`.

* **Conversion explicite (*Casting*) :** Action volontaire du développeur via une fonction constructeur (ex: `int("10")`, `str(42)`).
* **Conversion implicite (*Coercion*) :** Prise en charge automatique par l'interpréteur Python lors d'une opération (ex: `3 + 2.0` devient automatiquement un `float` `5.0`).

Voici plusieurs exemples concrets pour illustrer la **conversion implicite** (*type promotion* ou *coercion*) et la **conversion explicite** (*casting*) en Python.

---

**Conversions Implicites (Prises en charge automatiquement par Python)**

Python convertit automatiquement les types pour éviter toute perte de précision ou d'information lors d'une opération mixte.

```python
# --- Entier + Flottant -> Flottant ---
resultat_addition = 3 + 4.5
# 3 (int) est promu en 3.0 (float) -> résultat : 7.5 (float)

# --- Division standard d'entiers -> Flottant ---
resultat_division = 10 / 2
# Même si la division est exacte, / renvoie toujours un float -> résultat : 5.0 (float)

# --- Entier + Complexe -> Complexe ---
resultat_complexe = 5 + (2 + 3j)
# 5 (int) est converti en (5 + 0j) -> résultat : (7 + 3j) (complex)

# --- Évaluation booléenne implicite (Contexte logique) ---
# Dans un 'if' ou 'while', les types non-booléens sont évalués implicitement en booléens
compteur = 0
if not compteur:
    # 0 est évalué implicitement comme False -> 'not False' devient True
    print("Le compteur est vide")

```

---

**Conversions Explicites (*Casting* volontaire par le développeur)**

Lorsque Python refuse d'effectuer la conversion automatique (pour éviter des ambiguïtés), vous devez utiliser les fonctions constructeurs (`int()`, `float()`, `str()`, etc.).

```python
# --- 1. Chaîne vers Entier / Flottant ---
age_str = "25"
age_num = int(age_str)          # "25" (str) -> 25 (int)

prix_str = "19.99"
prix_num = float(prix_str)      # "19.99" (str) -> 19.99 (float)

# --- 2. Flottant vers Entier (Troncature) ---
note = 15.85
note_entiere = int(note)        # 15.85 -> 15 (la partie décimale est coupée, pas d'arrondi)

# --- 3. Nombre vers Chaîne (Concaténation) ---
score = 100
# print("Score : " + score)     # Erreur ! TypeError
message = "Score : " + str(score)  # Correct : "Score : 100"

# --- 4. Conversions entre Collections ---
liste_doublons = [1, 2, 2, 3, 4, 4]
ensemble_uniques = set(liste_doublons)   # [1, 2, 2, 3, 4, 4] -> {1, 2, 3, 4}
liste_nettoyee = list(ensemble_uniques)  # {1, 2, 3, 4} -> [1, 2, 3, 4]

```

> 💡 Privilégiez toujours les conversions explicites pour rendre votre code prévisible et éviter les ambiguïtés de calcul entre types numériques.

---

## Exemple de synthèse

```python
# Programme complet illustrant le casting et la conversion de données
prix_article_str = "49.99"  # Donnée brute sous forme de texte
quantite_str = "3"          # Donnée brute sous forme de texte

# Conversions explicites pour permettre les calculs arithmétiques
prix_unit = float(prix_article_str)
quantite = int(quantite_str)

# Conversion implicite lors du calcul du sous-total
sous_total = prix_unit * quantite  # float * int donne un float

# Conversion explicite inverse pour concaténation textuelle dans le message final
message = "Montant total à régler : " + str(sous_total) + " €"
print(message)

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script qui prend une chaîne de caractères représentant un prix avec des décimales, la convertit en type `float`, lui applique une taxe de 20%, puis convertit le résultat final en `str` pour l'afficher avec un message explicite.

**Exercice 2 :** Déclarez une variable entière et une variable flottante, effectuez une addition entre les deux, puis vérifiez et affichez le type de la variable résultante pour observer la conversion implicite de Python.


# Chapitre 6 : Manipulation des chaines de caractères

La manipulation des chaînes de caractères permet de traiter, formetter et analyser des données textuelles en Python. Maîtriser ces outils est indispensable pour interagir avec les utilisateurs et structurer des messages lisibles.
Dans ce chapitre :

* Gestion des chaines
* Formatage
* Slicing
* Expressions régulières

---

## Gestion des chaines

La gestion des chaînes de caractères repose sur l'utilisation de guillemets simples ou doubles pour déclarer du texte en mémoire. Python fournit de nombreuses méthodes intégrées pour transformer, nettoyer ou rechercher des motifs textuels.

Les **méthodes de gestion et de manipulation de chaînes de caractères (`str`)** en Python, classées par usage :

| Catégorie | Méthode | Description | Exemple | Résultat |
| --- | --- | --- | --- | --- |
| **Casse** | `s.lower()` | Convertit en minuscules | `"PY".lower()` | `"py"` |
| **Casse** | `s.upper()` | Convertit en majuscules | `"py".upper()` | `"PY"` |
| **Casse** | `s.capitalize()` | Première lettre en majuscule | `"python".capitalize()` | `"Python"` |
| **Casse** | `s.title()` | Majuscule au début de chaque mot | `"hello world".title()` | `"Hello World"` |
| **Nettoyage** | `s.strip()` | Supprime les espaces au début et à la fin | `"  dev  ".strip()` | `"dev"` |
| **Nettoyage** | `s.replace(a, b)` | Remplace la sous-chaîne `a` par `b` | `"1-2-3".replace("-", "/")` | `"1/2/3"` |
| **Découpage** | `s.split(sep)` | Découpe la chaîne en liste selon un séparateur | `"a,b,c".split(",")` | `['a', 'b', 'c']` |
| **Jonction** | `sep.join(seq)` | Sépare et concatène une liste de chaînes | `"-".join(['a', 'b'])` | `"a-b"` |
| **Recherche** | `s.find(sub)` | Renvoie l'index de la 1ʳᵉ occurrence (`-1` si absent) | `"python".find("th")` | `2` |
| **Recherche** | `s.count(sub)` | Compte le nombre d'occurrences d'une sous-chaîne | `"banana".count("a")` | `3` |
| **Inspection** | `s.startswith(x)` | Vérifie si la chaîne commence par `x` | `"image.png".startswith("img")` | `False` |
| **Inspection** | `s.endswith(x)` | Vérifie si la chaîne se termine par `x` | `"image.png".endswith(".png")` | `True` |
| **Validation** | `s.isdigit()` | `True` si tous les caractères sont des chiffres (`0-9`, indices) | `"123".isdigit()` | `True` |
| **Validation** | `s.isnumeric()` | `True` si caractères numériques (inclut fractions, chiffres romains) | `"½".isnumeric()` | `True` |
| **Validation** | `s.isalpha()` | `True` si uniquement des lettres alphabétiques | `"Code".isalpha()` | `True` |
| **Validation** | `s.isalnum()` | `True` si uniquement des caractères alphanumériques | `"Py3".isalnum()` | `True` |
| **Formatage** | `s.zfill(width)` | Complète avec des zéros à gauche | `"42".zfill(5)` | `"00042"` |

---

**Nettoyage et casse**

```python
s = "  Python  "

# strip() : Supprime les espaces (ou caractères) au début et à la fin
s.strip()               # "Python"

# lower() : Passe tout le texte en minuscules
"PyThOn".lower()        # "python"

# upper() : Passe tout le texte en majuscules
"python".upper()        # "PYTHON"

# capitalize() : Met la première lettre en majuscule
"python".capitalize()   # "Python"

```

---

**Séparation et jonction**

```python
# 5. split() : Découpe une chaîne en liste selon un séparateur (espace par défaut)
"a,b,c".split(",")      # ['a', 'b', 'c']

# 6. join() : Assemble les éléments d'une liste en une seule chaîne
"-".join(['a', 'b'])    # "a-b"

```

---

**Recherche et remplacement**

```python
s = "Bonjour tout le monde"

# 7. replace() : Remplace une sous-chaîne par une autre
s.replace("monde", "monde !")  # "Bonjour tout le monde !"

# 8. find() : Renvoie l'index de la première occurrence (-1 si non trouvé)
s.find("tout")                 # 8

# 9. count() : Compte le nombre d'occurrences d'une sous-chaîne
s.count("o")                   # 4

```

---

**Vérification de contenu (retournent un booléen)**

```python
# 10. startswith() : Vérifie si la chaîne commence par un motif
"main.py".startswith("main")   # True

# 11. endswith() : Vérifie si la chaîne se termine par un motif
"image.png".endswith(".png")   # True

# 12. isdigit() : Vérifie si la chaîne contient uniquement des chiffres
"12345".isdigit()              # True

```

> 💡 **Bonne pratique :** En Python, les chaînes de caractères étant **immuables**, aucune de ces méthodes ne modifie la chaîne d'origine. Elles renvoient toujours une nouvelle chaîne ou une nouvelle valeur.

> 💡 Les chaînes de caractères en Python sont immuables : toute modification textuelle génère un nouvel objet en mémoire plutôt que de modifier la chaîne originale.

---

## Formatage

Voici un exemple comparatif simple montrant comment insérer un texte (chaîne) et un nombre (entier ou flottant) avec l'ancien opérateur `%` et la méthode `.format()` :

```python
nom = "Alice"
age = 30
prix = 19.99

# Formatage avec l'opérateur % (ancien style - style C)
# %s = string, %d = integer, %.2f = float avec 2 décimales
message_percent = "Bonjour %s, vous avez %d ans. Total : %.2f €" % (nom, age, prix)
print(message_percent)

# Formatage avec la méthode .format() (style Python 2.6+)
# Les accolades {} servent de réceptacles
message_format = "Bonjour {}, vous avez {} ans. Total : {:.2f} €".format(nom, age, prix)
print(message_format)

# Variante avec clés nommées (très pratique pour la lisibilité)
message_nomme = "Bonjour {n}, vous avez {a} ans.".format(n=nom, a=age)
print(message_nomme)

```

---

**Résumé des spécificateurs courants**

* **`%s`** ou **`{}`** : Chaîne de caractères (*string*)
* **`%d`** ou **`{:d}`** : Entier (*integer*)
* **`%.2f`** ou **`{:.2f}`** : Nombre à virgule avec 2 décimales (*float*)

> 💡 **À retenir :** Dans du code moderne (Python 3.6+), on utilise majoritairement les **f-strings** (`f"Bonjour {nom}"`), mais la méthode `.format()` reste très utile quand le modèle de texte est stocké dans un fichier externe ou une variable.

Le formatage permet d'insérer dynamiquement des variables ou des expressions au sein d'une chaîne de caractères de manière lisible et performante. Les f-strings constituent la méthode moderne recommandée en Python.

```python
# Utilisation des f-strings pour l'interpolation de variables
langage = "Python"
version = 3.10
message = f"Apprentissage de {langage} en version {version}"

```

> 💡 Préférez toujours l'utilisation des f-strings par rapport aux anciennes méthodes de formatage (`%` ou `.format()`) pour gagner en lisibilité et en performance.

---

## Slicing

Le **slicing** (ou découpage) en Python est une technique qui permet d'extraire une sous-partie d'une séquence (chaîne de caractères, liste, tuple) sans modifier la séquence d'origine.

---

**Formule générale**

La syntaxe utilise des crochets séparés par deux-points (`:`), et non des virgules :

$$\mathbf{[début : fin : pas]}$$

---

**Signification des paramètres**

* **`début`** *(n)* : L'index du premier élément inclus. S'il est omis, la sélection commence au début (`0`).
* **`fin`** *(m)* : L'index du premier élément **exclu** (la sélection s'arrête juste avant cet index). S'il est omis, la sélection va jusqu'à la fin de la séquence.
* **`pas`** : Le saut entre chaque élément retenu (positif pour aller vers l'avant, négatif pour aller en arrière). Par défaut, il vaut `1`.

---

```python
texte = "Python"
# Index :  0   1   2   3   4   5
#         'P' 'y' 't' 'h' 'o' 'n'

# Extraction standard : du caractère index 0 à l'index 4 exclu
print(texte[0:4])       # "Pyth"

# Utilisation du pas : un caractère sur deux
print(texte[0:6:2])     # "Pto"

# Omision des bornes (équivalent à tout prendre) avec un pas de 2
print(texte[::2])       # "Pto"

# Inverser une chaîne (pas négatif)
print(texte[::-1])      # "nohtyP"

```

> 💡 **À retenir :** En Python, l'élément situé à l'index de **`fin`** n'est jamais inclus dans le résultat. La longueur du résultat extrait correspond généralement à $\text{fin} - \text{début}$ (si le pas vaut $1$).

> 💡 En Python, les indices de découpage commencent à zéro et l'indice de fin spécifié est toujours exclus du résultat extrait.

---

## Expressions régulières

Les expressions régulières permettent de rechercher, valider ou extraire des motifs complexes dans des chaînes de caractères en s'appuyant sur le module standard `re`.

Le module standard **`re`** permet de manipuler les expressions régulières (Regex) en Python pour rechercher, valider ou remplacer des motifs de texte.

Codification des expressions régulières (les motifs clés)

Une expression régulière utilise des caractères spéciaux pour définir des modèles de texte :

* **Classes de caractères :**
* `\d` : n'importe quel chiffre (équivalent à `[0-9]`).
* `\w` : n'importe quel caractère alfanumérique ou souligné (équivalent à `[a-zA-Z0-9_]`).
* `\s` : n'importe quel espace blanc (espace, tabulation, saut de ligne).
* `.` : n'importe quel caractère sauf le saut de ligne.


* **Quantificateurs :**
* `+` : 1 ou plusieurs fois.
* `*` : 0 ou plusieurs fois.
* `?` : 0 ou 1 fois (optionnel).
* `{n,m}` : entre $n$ et $m$ fois.


* **Ancres et groupes :**
* `^` : début de la chaîne.
* `$` : fin de la chaîne.
* `(...)` : groupe de capture.

---

**`re.search()` : Trouver la première occurrence**

Cherche le motif n'importe où dans la chaîne et renvoie un objet `Match` (ou `None`).

```python
import re

texte = "Le prix est de 49 euros."

#Cherche un ou plusieurs chiffres (\d+)
match = re.search(r"\d+", texte)

if match:
    print(match.group())  # "49"

```

**`re.findall()` : Extraire toutes les occurrences**

Renvoie une liste contenant toutes les correspondances trouvées dans la chaîne.

```python
texte = "Contact : info@test.fr ou support@societe.com"
# Motif simple pour capter une adresse email
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", texte)

print(emails)  # ['info@test.fr', 'support@societe.com']

```

**`re.sub()` : Rechercher et remplacer**

Remplacer un motif par un autre texte.

```python
texte = "Mon numéro est 0612345678"
# Masque les chiffres du numéro de téléphone
masque = re.sub(r"\d", "*", texte)

print(masque)  # "Mon numéro est **********"

```

**`re.match()` : Valider le début de la chaîne**

Vérifie si la chaîne **commence** par le motif spécifié (idéal pour la validation de format).

```python
code_postal = "75001 Paris"
# Vérifie si le texte commence par exactement 5 chiffres
valide = re.match(r"^\d{5}", code_postal)

if valide:
    print("Code postal valide :", valide.group())  # "75001"

```

> 💡 **Bonne pratique :** Préfixez toujours vos chaînes de motifs Regex avec la lettre `r` (ex: `r"\d+"`). Cela indique à Python qu'il s'agit d'une chaîne brute (*raw string*) et évite les conflits avec les caractères d'échappement comme `\n` ou `\t`.

---

## Exemple de synthèse

```python
import re

# Programme complet combinant gestion, formatage, slicing et expressions régulières
reference_brute = "   REF-9876-FR   "

# Gestion : nettoyage des espaces superflus et mise en majuscules
reference_nette = reference_brute.strip()

# Slicing : extraction de la portion numérique centrale
code_numerique = reference_nette[4:8]

# Expressions régulières : validation du format global
pattern = r"^REF-\d{4}-[A-Z]{2}$"
est_conforme = bool(re.match(pattern, reference_nette))

# Formatage : construction du message final avec une f-string
rapport = f"Référence : {reference_nette} | Code extrait : {code_numerique} | Conforme : {est_conforme}"
print(rapport)

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script qui prend une chaîne de caractères contenant des espaces superflus et du texte en minuscules, puis utilisez les méthodes de gestion pour la nettoyer et la mettre entièrement en majuscules.

**Exercice 2 :** Déclarez une chaîne contenant un numéro de téléphone sous la forme d'une phrase, puis utilisez le slicing pour extraire les deux premiers caractères et formotez un message personnalisé à l'aide d'une f-string.


# Chapitre 7 : Manipulation des données structurées - list, dict et set

La manipulation des données structurées permet d'organiser, de stocker et de parcourir efficacement des collections d'éléments en Python. Maîtriser ces structures est indispensable pour traiter des volumes d'informations complexes.
Dans ce chapitre :

* Gestion des listes
* Gestion des dictionnaires (dict)
* Gestion des ensembles (set)

---

## Gestion des listes

Les listes permettent de stocker une collection ordonnée d'éléments modifiables. Elles autorisent les doublons et offrent de nombreuses méthodes pour ajouter, supprimer ou trier des données en mémoire.

Voici une sélection concise des opérations indispensables sur les listes (méthodes standards et slicing), prêtes à être intégrées dans votre support de cours :

Les **méthodes de manipulation de listes (`list`)** en Python, classées par usage :

| Catégorie | Méthode | Description | Exemple (`l = [1, 2]`) | Résultat / État de `l` |
| --- | --- | --- | --- | --- |
| **Ajout** | `l.append(x)` | Ajoute l'élément `x` à la fin de la liste | `l.append(3)` | `[1, 2, 3]` |
| **Ajout** | `l.extend(iterable)` | Étend la liste en y ajoutant tous les éléments d'un itérable | `l.extend([3, 4])` | `[1, 2, 3, 4]` |
| **Ajout** | `l.insert(i, x)` | Insère l'élément `x` à l'index `i` spécifié | `l.insert(1, 9)` | `[1, 9, 2]` |
| **Suppression** | `l.pop([i])` | Retire et renvoie l'élément à l'index `i` (par défaut le dernier) | `val = l.pop()` | `val = 2`, `l = [1]` |
| **Suppression** | `l.remove(x)` | Supprime la première occurrence de la valeur `x` | `l.remove(1)` | `[2]` *(erreur si absent)* |
| **Suppression** | `l.clear()` | Supprime tous les éléments de la liste | `l.clear()` | `[]` |
| **Recherche** | `l.index(x)` | Renvoie l'index de la première occurrence de `x` | `[10, 20].index(20)` | `1` *(erreur si absent)* |
| **Recherche** | `l.count(x)` | Renvoie le nombre d'occurrences de la valeur `x` | `[1, 2, 1].count(1)` | `2` |
| **Organisation** | `l.sort()` | Trie la liste **en place** (modifie l'originale, renvoie `None`) | `[3, 1].sort()` | `[1, 3]` |
| **Organisation** | `l.reverse()` | Inverse l'ordre des éléments **en place** | `[1, 2].reverse()` | `[2, 1]` |
| **Copie** | `l.copy()` | Renvoie une copie superficielle (*shallow copy*) de la liste | `c = l.copy()` | `c = [1, 2]` |

Fonctions et méthodes essentielles sur les listes

```python
# Initialisation
outils = ["git", "docker", "vscode"]

# Ajout d'éléments
outils.append("python")              # Ajoute à la fin -> ['git', 'docker', 'vscode', 'python']
outils.insert(1, "bash")             # Insère à l'index 1 -> ['git', 'bash', 'docker', 'vscode', 'python']

# Suppression d'éléments
outils.remove("vscode")             # Supprime par valeur
element = outils.pop(0)              # Supprime et renvoie l'élément à l'index 0 ('git')

# Recherche et comptage
index = outils.index("docker")       # Renvoie l'index de la valeur (1)
total = outils.count("python")       # Compte le nombre d'occurrences (1)

# Tri et inversion
outils.sort()                        # Trie la liste sur place (ordre alphabétique)
outils.reverse()                     # Inverse l'ordre des éléments sur place

# Fonctions globales utiles
longueur = len(outils)               # Nombre d'éléments dans la liste
nombres = [10, 5, 20, 2]
print(min(nombres), max(nombres))    # Renvoie 2 et 20
print(sum(nombres))                  # Calcule la somme (37)

```

> 💡 **À retenir :** `.sort()` modifie directement la liste d'origine sans rien renvoyer. Pour obtenir une nouvelle liste triée sans modifier la première, utilisez `sorted(liste)`.

---

**Slicing appliqué aux listes**

La syntaxe `liste[début:fin:pas]` fonctionne exactement comme sur les chaînes de caractères :

```python
frameworks = ["Django", "Flask", "FastAPI", "Express", "Spring", "Angular"]
# Index :        0        1        2          3          4         5

# Extraction d'une sous-liste [début:fin]
backend = frameworks[0:3]           # ['Django', 'Flask', 'FastAPI'] (index 3 exclu)

# Raccourcis depuis le début ou jusqu'à la fin
premiers = frameworks[:2]           # ['Django', 'Flask']
derniers = frameworks[3:]           # ['Express', 'Spring', 'Angular']

# Utilisation d'index négatifs
trois_derniers = frameworks[-3:]    # ['Express', 'Spring', 'Angular']

# Extraire avec un pas
un_sur_deux = frameworks[::2]       # ['Django', 'FastAPI', 'Spring']

# Copie intégrale et inversion
copie_liste = frameworks[:]         # Crée une copie indépendante de la liste
liste_inversee = frameworks[::-1]   # Inverse toute la liste

```

**Parcourir avec l'index et la valeur (`enumerate`)**

```python
utilisateurs = ["Alice", "Bob", "Charlie"]

# Permet de récupérer l'index et la valeur à chaque itération
for index, nom in enumerate(utilisateurs, start=1):
    print(f"Utilisateur n°{index} : {nom}")

```

**Parcourir et filtrer avec une compréhension de liste**

```python
nombres = [12, 5, 8, 19, 3, 14]

# Crée une nouvelle liste contenant uniquement les nombres supérieurs à 10
nombres_grands = [n for n in nombres if n > 10]
print("Nombres > 10 :", nombres_grands)  # Résultat : [12, 19, 14]

```

> 💡 **Bonne pratique :** `copie = liste[:]` (ou `liste.copy()`) permet d'éviter les pièges de référence mémoire où la modification d'une liste affecte par erreur la seconde.

---

## Gestion des dict

Les dictionnaires stockent des données sous forme de paires clé-valeur, permettant un accès ultra-rapide aux valeurs grâce à leurs clés uniques. Ils sont parfaits pour représenter des objets ou des configurations.

Les **méthodes de manipulation de dictionnaires (`dict`)** en Python, classées par usage :

| Catégorie | Méthode | Description | Exemple (`d = {'a': 1, 'b': 2}`) | Résultat / État de `d` |
| --- | --- | --- | --- | --- |
| **Accès** | `d.get(k, def)` | Renvoie la valeur associée à la clé `k`, ou `def` si absente | `d.get('c', 0)` | `0` *(évite une `KeyError`)* |
| **Accès / Modification** | `d.setdefault(k, def)` | Renvoie la valeur de `k`. Si `k` n'existe pas, l'insère avec la valeur `def` | `d.setdefault('c', 3)` | Renvoie `3`, `d` devient `{'a': 1, 'b': 2, 'c': 3}` |
| **Mise à jour** | `d.update(autre)` | Fusionne un autre dictionnaire ou des couples clé-valeur dans `d` | `d.update({'b': 9, 'c': 3})` | `{'a': 1, 'b': 9, 'c': 3}` |
| **Suppression** | `d.pop(k, def)` | Supprime la clé `k` et renvoie sa valeur (ou `def` si absente) | `val = d.pop('a')` | `val = 1`, `d` devient `{'b': 2}` |
| **Suppression** | `d.popitem()` | Supprime et renvoie le dernier couple `(clé, valeur)` inséré | `k, v = d.popitem()` | `k, v = ('b', 2)`, `d` devient `{'a': 1}` |
| **Suppression** | `d.clear()` | Supprime tous les éléments du dictionnaire | `d.clear()` | `{}` |
| **Vue** | `d.keys()` | Renvoie une vue des clés du dictionnaire | `d.keys()` | `dict_keys(['a', 'b'])` |
| **Vue** | `d.values()` | Renvoie une vue des valeurs du dictionnaire | `d.values()` | `dict_values([1, 2])` |
| **Vue** | `d.items()` | Renvoie une vue des couples `(clé, valeur)` sous forme de tuples | `d.items()` | `dict_items([('a', 1), ('b', 2)])` |
| **Copie** | `d.copy()` | Renvoie une copie superficielle (*shallow copy*) du dictionnaire | `c = d.copy()` | `c = {'a': 1, 'b': 2}` |

* **Opérateur de fusion (Python 3.9+) :** En alternative à `.update()`, l'opérateur `|` permet de fusionner deux dictionnaires pour en créer un nouveau (`d3 = d1 | d2`).
Fonctions et méthodes essentielles sur les **dictionnaires** (méthodes essentielles et parcours), prêts pour votre support :

Fonctions et méthodes essentielles sur les dictionnaires

```python
# Initialisation
user = {"id": 101, "nom": "Alice", "role": "Dev"}

# Accès sécurisé et modification
role = user.get("role", "Invité")     # Renvoie "Dev" (sans erreur si la clé n'existe pas)
user["email"] = "alice@test.fr"       # Ajoute une nouvelle clé-valeur
user["role"] = "Admin"                # Modifie la valeur d'une clé existante

# Fusion et mise à jour
user.update({"statut": "Actif", "age": 30})  # Ajoute/modifie plusieurs clés à la fois

# Suppression
email = user.pop("email", None)       # Supprime "email" et renvoie sa valeur
del user["age"]                       # Supprime directement la clé "age"

# 4. Vérification d'existence
existe = "nom" in user                # True (vérifie la présence d'une CLÉ)

```

> 💡 **À retenir :** L'accès direct via `user["inconnu"]` lève une erreur `KeyError` si la clé n'existe pas. Utilisez toujours la méthode `.get("clé", valeur_par_defaut)` pour sécuriser la lecture.

---

**Parcours et extraction (items, keys, values)**

```python
config = {"host": "localhost", "port": 8080, "debug": True}

# Extraction des clés, valeurs et couples
cles = config.keys()                  # dict_keys(['host', 'port', 'debug'])
valeurs = config.values()              # dict_values(['localhost', 8080, True])
couples = config.items()              # dict_items([('host', 'localhost'), ...])

# Parcours par clé-valeur (le plus utilisé)
for cle, valeur in config.items():
    print(f"{cle} -> {valeur}")

# Dictionnaire par compréhension (filtrage/transformation)
config_str = {k: str(v) for k, v in config.items() if k != "debug"}
# Résultat : {'host': 'localhost', 'port': '8080'}

```

Voici deux exemples pratiques pour parcourir un dictionnaire en Python :

**Parcourir les clés et les valeurs simultanément (`items()`)**

C'est la méthode la plus utilisée pour traiter chaque couple clé-valeur :

```python
serveur = {"nom": "Web-01", "ip": "192.168.1.10", "statut": "Actif"}

# Utilisation de .items() pour dépaqueter la clé et la valeur
for cle, valeur in serveur.items():
    print(f"{cle.capitalize()} : {valeur}")

```

---

### Parcourir et transformer avec une dictionnaire compréhension

Permet de filtrer ou modifier les entrées d'un dictionnaire de façon concise :

```python
prix_ht = {"article_1": 10.0, "article_2": 25.0, "article_3": 5.0}

# Application de la TVA (20%) sur chaque valeur
prix_ttc = {cle: valeur * 1.20 for cle, valeur in prix_ht.items()}
print("Prix TTC :", prix_ttc)  # {'article_1': 12.0, 'article_2': 30.0, 'article_3': 6.0}

```

> 💡 **Bonne pratique :** Depuis Python 3.7, l'ordre d'insertion des clés dans un dictionnaire est garanti garanti lors des parcours.
> 💡 Privilégiez l'utilisation de la méthode `.get()` pour interroger un dictionnaire lorsque la clé recherchée est susceptible de ne pas y figurer.

---

## Gestion des set

Les ensembles (`set`) stockent des collections non ordonnées d'éléments uniques. Ils suppriment automatiquement les doublons et s'avèrent extrêmement utiles pour effectuer des opérations mathématiques ensemblistes (union, intersection).

Voici les exemples sur les **ensembles (`set`)** (opérations d'ensemble et méthodes clés), prêts pour votre support :

**Fonctions et méthodes essentielles sur les ensembles**

```python
# Initialisation (collection d'éléments uniques, non ordonnés)
langages = {"Python", "Java", "C++"}

# Ajout d'éléments
langages.add("TypeScript")           # Ajoute un élément
langages.add("Python")               # Ignoré (aucun doublon autorisé)

# Suppression d'éléments
langages.remove("Java")              # Supprime 'Java' (lève KeyError si absent)
langages.discard("Rust")             # Supprime 'Rust' (ne fait rien si absent, pas d'erreur)

# Conversion pour dédoublonner une liste
doublons = [1, 2, 2, 3, 4, 4, 4]
uniques = set(doublons)              # {1, 2, 3, 4}
liste_propre = list(uniques)         # [1, 2, 3, 4]

```

> 💡 **À retenir :** Un `set` ne contient **aucun doublon** et n'est pas ordonné. Il est impossible d'accéder à ses éléments par un index comme `ensemble[0]`.

---

**Opérations mathématiques sur les ensembles**

```python
dev_backend = {"Python", "Java", "SQL", "Docker"}
dev_frontend = {"JavaScript", "TypeScript", "HTML", "Docker"}

# Union (|) : Tous les éléments des deux ensembles sans doublons
tous = dev_backend | dev_frontend     
# {'Python', 'Java', 'SQL', 'Docker', 'JavaScript', 'TypeScript', 'HTML'}

# Intersection (&) : Éléments communs aux deux ensembles
communs = dev_backend & dev_frontend  
# {'Docker'}

# Différence (-) : Éléments présents uniquement dans le premier
seule_backend = dev_backend - dev_frontend 
# {'Python', 'Java', 'SQL'}

# Différence symétrique (^) : Éléments non communs
exclusifs = dev_backend ^ dev_frontend 
# {'Python', 'Java', 'SQL', 'JavaScript', 'TypeScript', 'HTML'}

```

Voici deux exemples pratiques pour parcourir un **ensemble (`set`)** en Python :

**Parcourir directement les éléments (`for ... in`)**

Comme un `set` est une collection non ordonnée, le parcours se fait élément par élément :

```python
langages = {"Python", "Java", "TypeScript", "C++"}

for langage in langages:
    print(f"Langage disponible : {langage}")

```
---

**Parcourir et filtrer avec une compréhension d'ensemble (*Set Comprehension*)**

Permet de créer un nouvel ensemble en appliquant une condition ou une transformation lors du parcours :

```python
nombres = {2, 8, 15, 22, 3, 40}

# On extrait uniquement les nombres pairs supérieurs à 10
pairs_grands = {n for n in nombres if n % 2 == 0 and n > 10}

print(pairs_grands)  # Résultat : {40, 8, 22} (l'ordre d'affichage peut varier)

```

> 💡 **À retenir :** Un `set` ne conserve pas l'ordre d'insertion des éléments et n'a pas d'index. On ne peut donc pas utiliser `enumerate()` pour obtenir des index fixes comme sur une liste.

> 💡 **Bonne pratique :** Tester la présence d'un élément dans un `set` avec `if "Python" in ensemble:` est extrêmement rapide (complexité $O(1)$) comparé à une liste (complexité $O(n)$).

> 💡 Utilisez les opérateurs ensemblistes comme `&` pour l'intersection ou `|` pour l'union afin de comparer rapidement des collections de données.

---

## Exemple de synthèse

```python
# Programme complet combinant listes, dictionnaires et ensembles
# Gestion des listes : stockage des identifiants de connexions successives
historique_connexions = ["user_1", "user_2", "user_1", "user_3"]

# Gestion des set : extraction des utilisateurs uniques sans doublons
utilisateurs_uniques = set(historique_connexions)

# Gestion des dict : association d'un statut à chaque utilisateur unique
statuts_utilisateurs = {
    "user_1": "actif",
    "user_2": "inactif",
    "user_3": "actif"
}

print(f"Utilisateurs uniques : {utilisateurs_uniques}")
print(f"Statut de user_1 : {statuts_utilisateurs.get('user_1')}")

```

## Exercices de fin de chapitre

**Exercice 1 :** Créer une liste de 10 valeurs aleatoires `random.randrange(100)`, parcourrir le tableau et compter les nombres paires et les impaires

**Exercice 2 :** Créer deux listes noms = ["toto1", "toto2"...] et ages [1,2 ...], les assembler dans une boucles pour former un dict() nom/age 

**Exercice 3 :** Créer une liste de 10 valeurs aleatoires `random.randrange(100)`, parcourrir le tableau et créer deux tableaux contenants les paires et les impaires séparemment


# Chapitre 8 : Les instructions contrôles

Les instructions de contrôle permettent d'orienter le flux d'exécution d'un programme en fonction de conditions et de répéter des blocs de instructions. Maîtriser ces structures est indispensable pour automatiser des tâches complexes.
Dans ce chapitre :

* Structures conditionnelles `if`/`else` et `match`
* Boucles itératives (`for`/`else`, `while`)
* Itérations avancées (`range`, `zip`, `items()`)

---

## Structure conditionnelles if/else/then,match

Les structures conditionnelles permettent d'exécuter des blocs de code différents selon la validité d'une ou plusieurs conditions logiques. L'instruction `match`, introduite récemment, facilite les aiguillages complexes par motif.

Voici la forme générale des structures conditionnelles `if / elif / else` en Python :

**Forme générale**

```python
if condition_1:
    # Bloc exécuté si condition_1 est True
    instructions
elif condition_2:
    # Bloc exécuté si condition_1 est False ET condition_2 est True
    instructions
elif condition_3:
    # Autre condition optionnelle...
    instructions
else:
    # Bloc exécuté si AUCUNE des conditions précédentes n'est True
    instructions

```

---

**Points clés à retenir**

* **`if`** : Obligatoire (un seul par bloc). C'est le point d'entrée de la condition.
* **`elif`** *(contraction de "else if")* : Optionnel. Il peut y en avoir zéro, un ou plusieurs à la suite.
* **`else`** : Optionnel (un seul à la fin). Il capture tous les cas restants.
* **Les deux-points `:**` : Indispensables après chaque clause (`if`, `elif`, `else`).
* **L'indentation** *(4 espaces)* : Obligatoire. C'est elle qui délimite le bloc de code rattaché à chaque condition.

---

```python
note = 14

if note >= 16:
    print("Mention Très Bien")
elif note >= 14:
    print("Mention Bien")
elif note >= 12:
    print("Mention Assez Bien")
elif note >= 10:
    print("Admis")
else:
    print("Ajourné")

```

> 💡 **Variante (Forme condensée / Opérateur ternaire) :**
> Pour une affectation simple selon une seule condition, vous pouvez écrire :
> `statut = "Majeur" if age >= 18 else "Mineur"`

---

## Structure match

L'instruction `match` réalise un filtrage par motif (*pattern matching*), permettant de comparer une valeur à plusieurs structures ou cas possibles de manière très lisible.

```python
# Utilisation de match pour aiguiller selon une commande
commande = "quit"
match commande:
    case "start":
        print("Démarrage...")
    case "quit":
        print("Arrêt...")
    case _:
        print("Commande inconnue")

```

> 💡 Utilisez le motif universel `_` comme dernier cas dans un `match` pour capturer toutes les valeurs non gérées explicitement.

---

## Boucles - for/else

La boucle `for` permet de parcourir séquentiellement les éléments d'une collection. En Python, elle peut être associée à un bloc `else` optionnel qui s'exécute si la boucle s'est terminée sans interruption par un `break`.

```python
# Parcours d'une liste avec une boucle for
nombres = [1, 2, 3]
for n in nombres:
    print(n)

```

> 💡 Utilisez le bloc `else` d'une boucle `for` pour exécuter du code de validation si aucun élément recherché n'a déclenché de rupture anticipée.

---

## Boucles - while

La boucle `while` répète l'exécution d'un bloc d'instructions tant qu'une condition booléenne associée reste évaluée à `True`. Elle est idéale lorsque le nombre d'itérations n'est pas connu à l'avance.

```python
# Compteur avec une boucle while
compteur = 0
while compteur < 3:
    print(compteur)
    compteur += 1

```

> 💡 Veillez à toujours faire évoluer la variable de condition à l'intérieur d'une boucle `while` pour éviter les boucles infinies.

---

## Boucles - avec range

L'association d'une boucle `for` avec la fonction `range()` permet de répéter un bloc d'instructions un nombre précis de fois en générant une séquence numérique efficace.

```python
# Répétition d'une action à l'aide de range
for i in range(3):
    print(f"Itération numéro {i}")

```

> 💡 La fonction `range(debut, fin, pas)` accepte des arguments optionnels pour démarrer à un autre indice ou parcourir les éléments par pas spécifiques.

---

## Boucles - avec zip

La fonction `zip()` permet de parcourir simultanément plusieurs collections en assemblant leurs éléments sous forme de tuples, ce qui simplifie le traitement croisé de données.

```python
# Itération conjointe sur deux listes
noms = ["Alice", "Bob"]
scores = [85, 92]
for nom, score in zip(noms, scores):
    print(f"{nom} a obtenu {score} points")

```

> 💡 Si les collections passées à `zip()` n'ont pas la même longueur, l'itération s'arrête automatiquement dès que la plus courte est épuisée.

---

## Boucles - avec items() pour les dictionnaires

La méthode `.items()` permet de parcourir à la fois les clés et les valeurs d'un dictionnaire lors d'une même boucle `for`, optimisant la lecture des données structurées.

```python
# Parcours des clés et valeurs d'un dictionnaire
parametres = {"theme": "sombre", "volume": 80}
for cle, valeur in parametres.items():
    print(f"{cle} : {valeur}")

```

> 💡 Utilisez `.items()` dès que vous avez besoin de manipuler simultanément la clé et sa valeur associée pour éviter des appels d'accès superflus.

---

## Exemple de synthèse

```python
# Programme complet combinant conditions, boucles, range, zip et items
utilisateurs = ["Alice", "Bob", "Charlie"]
points = [45, 60, 30]

# Boucle avec range pour un affichage numéroté
for i in range(len(utilisateurs)):
    print(f"Rang {i + 1}")

# Boucle avec zip pour associer utilisateurs et scores
for user, score in zip(utilisateurs, points):
    # 3. Structure conditionnelle classique
    if score >= 50:
        niveau = "Expert"
    else:
        niveau = "Débutant"
    print(f"{user} ({niveau}) avec {score} pts")

# Boucle avec items() pour parcourir un dictionnaire de configuration
config = {"mode": "admin", "debug": True}
for parametre, etat in config.items():
    match parametre:
        case "mode":
            print(f"Mode actif : {etat}")
        case "debug":
            print(f"Mode débogage activé : {etat}")

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script qui produit, au moyen d'une boucle, une liste de 5 listes  = [['TOTO1',1],['TOTO2',2],...['TOTO5',5]]. Ensuite pourcourir cette liste et afficher que le noms TOTO1, TOTO2...

**Exercice 2 :** Écrivez un script qui produit, au moyen d'une boucle, une liste de 5 dict  = [{'nom':'TOTO1','age' : 1},...{'nom':'TOTO5','age' : 5}]. Ensuite pourcourir cette liste et afficher que le noms TOTO1, TOTO2...

**Exercice 2 :** Créez un dictionnaire associant des noms de fruits à leur prix, puis utilisez la méthode `.items()` dans une boucle pour afficher chaque fruit et son prix avec une structure conditionnelle vérifiant s'il est supérieur à un certain seuil.


# Chapitre 9 : Les fonctions et passage d'arguments

Les fonctions permettent de modulariser le code en regroupant des instructions réutilisables sous un même nom. Maîtriser le passage d'arguments et les structures de retour est indispensable pour concevoir des programmes propres et maintenables.
Dans ce chapitre :

* Définition des fonctions, arguments, passage et valeur de retour (`return`)
* Arguments et valeurs par défaut
* Arguments variables via les tuples, `*args` et `**kwargs`
* Fonctions en tant qu'arguments (délégués)

---

## Les fonctions, arguments , passage par valeur, return

Une fonction se déclare avec le mot-clé `def` suivi d'un nom et de parenthèses. Elle accepte des arguments en entrée et peut renvoyer un résultat grâce à l'instruction `return`.

```python
# Déclaration d'une fonction simple avec retour
def additionner(a, b):
    resultat = a + b
    return resultat

# Appel
r = additionner (10,20)
print(r)

```

> 💡 En Python, les objets sont passés par affectation : modifier un objet mutable à l'intérieur d'une fonction se répercute en dehors, contrairement aux objets immuables.

---

## Arguments et valeurs par défaut

Les arguments par défaut permettent de définir une valeur de repli lorsqu'un paramètre n'est pas explicitement fourni lors de l'appel de la fonction.

```python
# Fonction avec un argument doté d'une valeur par défaut
def saluer(nom, message="Bonjour"):
    return f"{message}, {nom} !"

# Appel 
r = saluer("Karim", "Hello")
print(r) # Hello Karim
r = saluer("Karim")
print(r) Bonjour Karim
```

> 💡 Ne jamais utiliser d'objets mutables (comme des listes ou des dictionnaires) comme valeurs par défaut d'une fonction, car leur état serait conservé entre les appels successifs.

---

## Arguments en tant que tuple

Il est possible de regrouper plusieurs valeurs d'arguments dans un tuple pour les manipuler de manière globale au sein de la fonction.

```python
# Fonction acceptant un tuple d'éléments regroupés
def afficher_coordonnees(coord):
    x, y = coord
    return f"Position X: {x}, Y: {y}"

# Appel
r = afficher_coordonnees((123, 456))
print(r)
```

> 💡 Utilisez l'emballage de tuples lorsque vos données possèdent une structure fixe et ordonnée que vous souhaitez traiter en bloc.

---

## Arguments avec *args

La syntaxe `*args` permet de transmettre un nombre variable d'arguments positionnels non nommés à une fonction, qui les récupère automatiquement sous forme de tuple.

```python
# Fonction acceptant un nombre indéfini d'arguments positionnels
def sommer_tout(*args):
    return sum(args)

# Appels
r = sommer_tout(11,22)
print(r)
r = sommer_tout(11,22,33,44)
print(r)

```

> 💡 Le nom `args` est une convention en Python, mais c'est l'astérisque `*` qui indique au langage de capturer tous les arguments positionnels excédentaires.

---

## Arguments *kargs

La syntaxe `**kwargs` (souvent appelée `kargs`) permet de récupérer un nombre variable d'arguments nommés sous la forme d'un dictionnaire au sein de la fonction.

```python
# Fonction acceptant des arguments nommés dynamiques
def configurer(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle} = {valeur}")

# --- Appels directs avec arguments nommés ---
print("--- Configuration 1 ---")
configurer(hôte="localhost", port=8080, debug=True)

# --- Appel avec un dictionnaire déballé (unpacking avec **) ---
print("\n--- Configuration 2 ---")
options = {
    "base_de_donnees": "postgres",
    "utilisateur": "admin",
    "timeout": 30
}
configurer(**options)

# --- Appel sans argument (kwargs sera un dictionnaire vide {}) ---
print("\n--- Configuration 3 ---")
configurer()
```

> 💡 L'utilisation conjointe de `*args` et `**kwargs` offre une flexibilité maximale pour créer des fonctions enveloppes (*wrappers*) ou des décorateurs.

---

## Fonction en tant qu'argument (delegate)

En Python, les fonctions sont des objets de première classe, ce qui signifie qu'elles peuvent être passées en tant qu'arguments à d'autres fonctions, agissant ainsi comme des délégués.

```python
# Utilisation d'une fonction en tant qu'argument
def appliquer_operation(operation, x, y):
    return operation(x, y)

# lambda a, b: a * b  equivalent de def <anonyme> (a, b) : return a * b
resultat = appliquer_operation(lambda a, b: a * b, 4, 5)
print(resultat)

```
Les arguments en tant que tuple 

```python
# La fonction accepte désormais un tuple en paramètre
def appliquer_operation(operation, donnees):
    # DÉSTRUCTURATION DU TUPLE : unpack des valeurs dans a et b
    a, b = donnees
    return operation(a, b)

# Appel avec un tuple (4, 5) transmis comme argument unique
resultat = appliquer_operation(lambda a, b: a * b, (4, 5))

print(resultat)  # Affiche : 20
```

> 💡 Passer des fonctions en argument est la base de la programmation fonctionnelle et permet de concevoir des algorithmes hautement génériques et réutilisables.

---

## Exemple de synthèse

```python
# Programme complet combinant fonctions, valeurs par défaut, *args, **kwargs et délégués

def calculer_total_remise(taux=0.1, *montants, **details):
    """Calcule un total avec *args et affiche les options via **kwargs."""
    sous_total = sum(montants)
    total_net = sous_total * (1 - taux)
    
    print(f"Facture pour {details.get('client', 'Client inconnu')}")
    print(f"Sous-total : {sous_total}€ | Net : {total_net}€")
    return total_net

# Fonction déléguée à passer en paramètre
def formater_monnaie(montant):
    return f"{montant:.2f} EUR"

# Appel de la fonction principale avec différents types d'arguments
montant_final = calculer_total_remise(0.2, 100.0, 50.0, 25.0, client="Alice", mode="express")
print("Format final :", formater_monnaie(montant_final))

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez une fonction qui accepte un nombre indéfini d'entiers via `*args` et retourne leur moyenne arithmétique.

**Exercice 2 :** Créez une fonction qui prend en paramètre une fonction mathématique et deux nombres, puis applique cette fonction sur les deux nombres pour retourner le résultat.


# Chapitre 10 : Traiter une masse de données

Le traitement de masses de données permet d'appliquer des transformations et des filtres performants sur des collections en Python. Maîtriser ces outils fonctionnels est indispensable pour manipuler efficacement des flux d'informations importants.
Dans ce chapitre :

* Fonctions anonymes `lambda`
* Filtrage de données avec `filter`
* Transformation de données avec `map`
* Agrégation de données avec `reduce`

---

## Fonction anonyme Lambda

Une fonction anonyme, introduite par le mot-clé `lambda`, permet de définir rapidement une fonction compacte sans nom sur une seule ligne de code. Elle est idéale pour des traitements courts et ponctuels. Au lieu de créer une fonction au moyen de def et la documenter, on préfère utiliser une lambda qui est une fonction sans nom et utilisée à la volée et peut être une fois.

```python
# Déclaration et appel d'une fonction lambda pour calculer le carré
carre = lambda x: x ** 2
resultat = carre(5)
print(resultat) #25

# fonction lambda
print(lambda x :  x* x)
<function <lambda> at 0x000001700E078D60>

# créer une lambda et l'appeler dans la foulée
print((lambda x :  x* x) (10))
100

# Vérifier si un nombre est pair ou impair
>pair_ou_impair = lambda x: "Pair" if x % 2 == 0 else "Impair"
>print(pair_ou_impair(4))  # Pair
>print(pair_ou_impair(7))  # Impair

# Tri d'une liste de tuples (nom, âge) selon l'âge (2ᵉ élément)
personnes = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
personnes.sort(key=lambda p: p[1])
print(personnes)  # [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

# Tri d'une liste de dictionnaires selon la longueur de la valeur
produits = [{"nom": "Clavier"}, {"nom": "Écran"}, {"nom": "Souris"}]
produits_tries = sorted(produits, key=lambda d: len(d["nom"]))
print(produits_tries)  # [{'nom': 'Écran'}, {'nom': 'Souris'}, {'nom': 'Clavier'}]
```

> 💡 Utilisez les fonctions `lambda` principalement comme arguments pour des fonctions de traitement de collections comme `map` ou `filter`.

---

## Traitement avec filter

La fonction `filter()` permet de filtrer les éléments d'une collection en évaluant chaque élément à l'aide d'une fonction conditionnelle qui retourne un booléen.

```python

# Filtrage des nombres pairs d'une liste
nombres = [1, 2, 3, 4, 5, 6]
pairs = list(filter(lambda x: x % 2 == 0, nombres)) #[2, 4, 6]

# trier la liste de chaînes sur leur longueur
mots = ["Python", "C++", "JavaScript", "Go"]
# Trouve le mot le plus long
mot_long = max(mots, key=lambda s : len(s))
print(mot_long)  # "JavaScript"

# avec une dictionnaire
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Erreur : division par zéro"
}
print(operations["+"](10, 5))  # 15
print(operations["/"](10, 0))  # Erreur : division par zéro

```

> 💡 Le résultat retourné par `filter()` en Python est un itérateur, pensez à le convertir explicitement en `list` ou `tuple` pour exploiter les données.

---

## Traitement avec map

La fonction `map()` applique une fonction spécifique à l'ensemble des éléments d'une collection itérable, transformant ainsi les données en une seule passe.

```python
# Application d'une transformation pour multiplier par 2 chaque élément
valeurs = [1, 2, 3, 4]
doubles = list(map(lambda x: x * 2, valeurs))  #[2, 4, 6, 8]

# --- map() : Appliquer une opération sur chaque élément (ex: doubler) ---
doubles = list(map(lambda x: x * 2, nombres))
print(doubles)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

```

> 💡 Les compréhensions de listes constituent souvent une alternative plus lisible et idiomatique aux fonctions `map()` en Python.

---

## Traitement avec reduce

La fonction `reduce()`, issue du module `functools`, permet de réduire une collection de données à une valeur unique en appliquant cumulativement une fonction binaire de manière séquentielle.

```python
from functools import reduce

# Calcul de la somme des éléments d'une liste par réduction
nombres = [1, 2, 3, 4]
somme_totale = reduce(lambda x, y: x + y, nombres) #10

```

> 💡 Pensez à importer `reduce` depuis le module `functools` avant de l'utiliser, car cette fonction n'est plus intégrée directement dans l'espace de noms global de Python.

---

## Exemple de synthèse

```python
from functools import reduce

# Programme complet combinant lambda, filter, map et reduce sur une masse de données
prix_articles = [12.5, 45.0, 8.0, 100.0, 32.5]

# 1. Filtrer les articles dont le prix est supérieur à 15.0 via filter et lambda
articles_cibles = list(filter(lambda p: p > 15.0, prix_articles))

# 2. Appliquer une remise de 10% sur ces articles via map et lambda
prix_remises = list(map(lambda p: p * 0.9, articles_cibles))

# 3. Calculer le montant total cumulé de ces articles via reduce et lambda
montant_global = reduce(lambda total, p: total + p, prix_remises, 0.0)

print(f"Articles remisés : {prix_remises}")
print(f"Montant global de la commande : {montant_global:.2f} €")

```

## Exercices de fin de chapitre

**Exercice 1 :** Utilisez la fonction `filter()` associée à une expression `lambda` pour extraire uniquement les mots de longueur supérieure à 5 caractères d'une liste de chaînes.

**Exercice 2 :** Importez `reduce` depuis `functools` et écrivez un script qui calcule le produit de tous les éléments d'une liste d'entiers.


# Chapitre 11 : Les générateurs

Les générateurs permettent de produire des séquences de valeurs à la demande sans stocker l'intégralité des données en mémoire. Maîtriser ces concepts est indispensable pour optimiser l'efficacité de vos programmes lors du traitement de grands volumes d'informations.
Dans ce chapitre :

* Boucle et instruction `yield`
* Générateurs prédéfinis

---

## Boucle et instruction yield

L'instruction `yield` permet à une fonction de retourner une valeur tout en suspendant son état d'exécution, transformant ainsi la fonction en un générateur capable de reprendre là où il s'était arrêté.

```python
# Définition d'une fonction génératrice simple
def generer_nombres(limite):
    n = 0
    while n < limite:
        yield n
        n += 1

print ( generer_nombres) # <function generer_nombres at 0x000001700E078E00>
list( generer_nombres(5)) # [0, 1, 2, 3, 4]

# itération sur le générateur
for i in generer_nombres(5): print (i)  # 0 1 2 3 4

# opérateur next() et détection de StopIteration
g = generer_nombres(3)
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
print(next(g))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

```

> 💡 Contrairement à `return`, l'instruction `yield` conserve l'état local de la fonction entre chaque itération, ce qui économise considérablement la mémoire vive.

---

## Générateur prédéfinis

Les générateurs prédéfinis englobent les expressions génératrices et les structures intégrées de Python qui produisent des flux d'éléments de manière paresseuse, évitant l'allocation préalable d'une collection complète.

```python
# Utilisation d'une expression génératrice pour un calcul optimisé en mémoire
carres_gen = (x ** 2 for x in range(5))
premier_element = next(carres_gen)

```

> 💡 Privilégiez les expressions génératrices entre parenthèses plutôt que les compréhensions de listes dès que vous manipulez des flux volumineux dont vous n'avez pas besoin de stocker l'ensemble des résultats simultanément.

---

## Exemple de synthèse

```python
# Programme complet combinant la création d'un générateur avec yield et un générateur prédéfini

def lecteur_lignes_simule(donnees):
    """Générateur personnalisé pour traiter des lignes de texte à la demande."""
    for ligne in donnees:
        # Instruction yield pour suspendre et renvoyer la ligne nettoyée
        yield ligne.strip().upper()

flux_brut = ["  premiere ligne  ", "  seconde ligne  ", "  troisieme ligne  "]

# Utilisation du générateur personnalisé
gen_personnalise = lecteur_lignes_simule(flux_brut)

# Utilisation d'un générateur prédéfini (enumerate) associé
for index, texte_traite in enumerate(gen_personnalise, start=1):
    print(f"Ligne {index} : {texte_traite}")

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez une fonction génératrice utilisant `yield` pour produire les nombres pairs jusqu'à une limite passée en paramètre, puis parcourez ce générateur avec une boucle `for`.

**Exercice 2 :** Créez une expression génératrice qui calcule les carrés des nombres de 1 à 10, et récupérez les valeurs un par un à l'aide de la fonction `next()`.


# Chapitre 12 : Un code plus robuste en prenant en compte les erreurs

La gestion des erreurs permet d'anticiper et de traiter les incidents d'exécution pour empêcher l'arrêt brutal d'un programme en Python. Maîtriser ces mécanismes est indispensable pour concevoir des applications fiables et résilientes.
Dans ce chapitre :

* Gestion des exceptions (`try`, `except`, `finally`) et levée d'exceptions (`raise`)
* Utilisation de l'instruction `finally`
* Émission personnalisée d'une exception

---

## Gestion des exceptions : try catch finally et throw

La gestion des exceptions repose sur le bloc `try` pour surveiller le code à risque et `except` pour intercepter les erreurs survenues. En Python, le mot-clé `raise` équivaut au `throw` des autres langages pour émettre une exception. On peut intercepter une exception précise ZeroDivisionError pour la traiter ou intercepter toutes les exceptions dans un même traitement

```python
# Interception d'une division par zéro
try:
    resultat = 10 / 0
    i+=1  # incrémenter une variable i qui n'existe pas 
except ZeroDivisionError:
    print("Erreur : Division par zéro impossible")
except Exception as e:
    print("Problème ", e)

# Plus de division par zéro mais "Problème  name 'i' is not defined"
try:
    resultat = 10 / 0
    i+=1  # incrémenter une variable i qui n'existe pas 
except ZeroDivisionError:
    print("Erreur : Division par zéro impossible")
except Exception as e:
    print("Problème ", e)

```

> 💡 Spécifiez toujours le type précis d'exception à intercepter dans votre bloc `except` plutôt que d'utiliser une clause globale muette qui masquerait des bugs inattendus.

---

## Instruction finally

L'instruction `finally` permet de définir un bloc de code qui s'exécute systématiquement à la fin, qu'une exception ait été levée ou non. Elle est idéale pour libérer des ressources (fichiers, connexions réseau).

```python
# Utilisation de finally pour la clôture des ressources
try:
    fichier = ouvrir_fichier("donnees.txt")
except FileNotFoundError:
    print("Fichier introuvable")
finally:
    fermer_fichier()  # Exécuté dans tous les cas

```

> 💡 Privilégiez l'utilisation du gestionnaire de contexte `with` lorsque c'est possible pour automatiser le nettoyage des ressources sans recourir explicitement à un bloc `finally`.

---

## Emettre une exception avec throw

Il est possible d'émettre volontairement une exception à l'aide de l'instruction `raise` (similaire à `throw`) pour signaler qu'une règle métier ou une condition critique n'est pas respectée.

```python
def traitement (eleve):
    if eleve['age'] < 0:
        #raise ValueError("L'âge ne peut pas être négatif") # ValueError: L'âge ne peut pas être négatif
        raise Exception ("L'âge ne peut pas être négatif")  # Exception: L'âge ne peut pas être négatif
    print(f"{eleve['nom']} -- {eleve['age']} ")

eleve = { 'nom' : 'karim', 'age' : 20}
traitement (eleve) # OK
eleve = { 'nom' : 'karim', 'age' : -20}
traitement (eleve) # exception prooduite qu'il faut intercepter dans un bloc try/except

```

> 💡 Créez vos propres classes d'exceptions personnalisées en héritant de la classe `Exception` de base pour affiner la gestion des erreurs spécifiques à votre domaine métier.
---
## Trace et log
Si la gestion des exceptions permet à un programme de réagir aux erreurs au moment où elles se produisent, **les traces et les logs** sont indispensables pour comprendre ce qui s'est passé en coulisses, analyser le comportement de l'application au fil du temps et déboguer plus facilement.

* **Les logs (journalisation) :** Un log est un enregistrement horodaté d'un événement précis survenu lors de l'exécution.Ils sont catégorisés par niveau de gravité (`INFO`, `WARNING`, `ERROR`, `CRITICAL`) pour filtrer les informations selon les besoins.Les logs permettent de garder un historique de la vie du système, notamment en environnement de production où l'affichage direct à l'écran n'est pas possible.
* **Les traces (ou *stack traces*) :** Lorsqu'une exception est levée (via `throw`) et non interceptée immédiatement, le langage génère une **trace d'exécution**. Cette trace agit comme un fil d'Ariane : elle liste la suite d'appels de fonctions, les fichiers et les numéros de lignes traversés jusqu'au point exact de la défaillance.

En pratique, la combinaison des deux est essentielle pour la robustesse : lors de la capture d'une exception dans un bloc `try/catch`, enregistrer la **trace** complète au sein d'un **log** de niveau `ERROR` permet aux développeurs de reconstituer précisément le contexte de la panne sans interrompre le service pour les autres utilisateurs.

Le niveau logger.exception() enregistre le message en niveau ERROR et inclut automatiquement la stack trace complète.

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    resultat = 10 / 0
except ZeroDivisionError:
    logger.exception("Une erreur de division par zéro est survenue")
```
Si tu souhaites utiliser un autre niveau de log (par exemple `CRITICAL` ou `WARNING`), ajoute le paramètre `exc_info=True`.

```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    logger.warning("Attention, calcul impossible !", exc_info=True)

```
Si tu as besoin de manipuler ou de mettre en forme la stack trace avant de la logger (ou sans lever d'exception), utilise le module standard `traceback`.

```python
import logging
import traceback

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    resultat = 10 / 0
except ZeroDivisionError:
    # Convertit la stack trace en str
    trace_str = traceback.format_exc()
    logger.error(f"Détail de l'erreur :\n{trace_str}")

```
Si tu souhaites afficher la chaîne d'appels courante dans les logs pour du débogage, sans qu'il n'y ait d'erreur :

```python
import logging
import traceback

def ma_fonction():
    # Capture la pile d'exécution actuelle
    stack = "".join(traceback.format_stack())
    logger.debug(f"Pile d'appel actuelle :\n{stack}")

ma_fonction()

```

---

## Exemple de synthèse

```python
# Programme complet combinant try, except, finally et la levée d'une exception avec raise

def convertir_et_diviser(valeur_str, diviseur_str):
    """Convertit deux chaînes en entiers et réalise une division sécurisée."""
    try:
        valeur = int(valeur_str)
        diviseur = int(diviseur_str)
        
        # Émission d'une exception personnalisée si le diviseur est nul
        if diviseur == 0:
            raise ZeroDivisionError("Le diviseur ne peut pas être égal à zéro.")
            
        quotient = valeur / diviseur
    except ValueError as e:
        return f"Erreur de format numérique : {e}"
    except ZeroDivisionError as e:
        return f"Erreur mathématique : {e}"
    finally:
        print("Fin de l'opération de calcul sécurisée.")
        
    return f"Résultat du calcul : {quotient}"

# Test de la fonction avec des valeurs littérales
print(convertir_et_diviser("100", "4"))
print(convertir_et_diviser("50", "0"))

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script qui demande à l'utilisateur de saisir un nombre, utilise un bloc `try...except` pour intercepter une éventuelle erreur de saisie (`ValueError`), et affiche un message adapté.

**Exercice 2 :** Créez une fonction qui vérifie si un mot de passe possède au moins 8 caractères. Si ce n'est pas le cas, utilisez `raise` pour émettre une exception personnalisée de type `ValueError`.


# Chapitre 13 : Script python en ligne de commande et passage d'arguments

La création de scripts en ligne de commande et le passage d'arguments permettent d'automatiser des tâches et d'interagir directement avec vos programmes Python depuis le terminal. Maîtriser ces outils est indispensable pour industrialiser vos développements.
Dans ce chapitre :

* Scripts et `__main__`
* Scripts et passage d'arguments
* Gestion de package avec `pip`
---

## Scripts et **main**

La structure `if __name__ == "__main__":` permet d'identifier si un fichier Python est exécuté directement comme un script principal ou importé comme un module dans un autre programme.

```python
# Vérification du point d'entrée principal du script
def executer_tache():
    print("Exécution du traitement principal...")

if __name__ == "__main__":
    executer_tache()

```

> 💡 Placez toujours le code d'exécution principale de vos scripts sous cette condition pour permettre la réutilisation propre de vos fonctions par d'autres modules.

---

## Scripts et passage d'arguments

Un script est un traitement spécifique en exploitation. Peut être qu'il faut lui passer des arguments de l'extérieur pour se réaliser (ex. sauvegarde.py <folder>). Dans ce cas il faut passer les nom du folder en argument au moment d'exécuter le script. Python permet de passer des arguments au moyen de sys.argv. On a deux modules possible sys et argparse.

script :  sauvegarde.py 
```python
def sauvegarde (folder):
    print(f"Je sauvegarde {folder}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2 :
        print("Il manque un argument ", sys.argv)
        sys.exit(1)
    # sys.argv[0] => sauvegarde.py 
    folder = sys.argv[1]
    sauvegarde (folder)
```
Erreur de lancement 
```bash
python sauvergarde.py
Il manque un argument  ['sauvergarde.py']
```

Lancement avec le repertoire "c:/"
```bash
python sauvergarde.py "c:/"
Je sauvegarde c:/
```

> 💡 Privilégiez l'utilisation du module `argparse` pour les scripts complexes afin de gérer automatiquement l'aide, les options obligatoires et les types d'arguments.

---

## Utilisation de argparse

```python
import argparse

def sauvegarde(folder):
    print(f"Je sauvegarde {folder}")


if __name__ == "__main__":
    # Création du parseur avec une description pour l'aide
    parser = argparse.ArgumentParser(
        description="Script de sauvegarde de dossier."
    )

    # Définition de l'argument obligatoire (positionnel)
    parser.add_argument(
        "folder",
        type=str,
        help="Chemin du dossier à sauvegarder",
    )

    # Analyse des arguments de la ligne de commande
    args = parser.parse_args()

    # Appel de la fonction avec l'argument récupéré
    sauvegarde(args.folder)

```

Lancement avec un argument en trop BB, le contôle est fait

```bash
python sauvergarde.py  AA BB
usage: sauvergarde.py [-h] folder
sauvergarde.py: error: unrecognized arguments: BB
```

Obtenir une aide 
```bash
python sauvergarde.py  -h
usage: sauvergarde.py [-h] folder

Script de sauvegarde de dossier.

positional arguments:
  folder      Chemin du dossier à sauvegarder

options:
  -h, --help  show this help message and exit
```
## Exemple de synthèse

```python
import sys

def traiter_commande_cli():
    """Simule un script en ligne de commande avec gestion des arguments."""
    # Vérification du point d'entrée principal
    if len(sys.argv) < 2:
        print("Erreur : Veuillez fournir un argument (ex: start ou stop).")
        return
    
    action = sys.argv[1].lower()
    
    # Traitement conditionnel basé sur l'argument reçu
    if action == "start":
        print("Démarrage du service en ligne de commande...")
    elif action == "stop":
        print("Arrêt du service demandé.")
    else:
        print(f"Action inconnue : {action}")

if __name__ == "__main__":
    traiter_commande_cli()

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script Python comportant une structure `if __name__ == "__main__":` qui affiche un message de bienvenue personnalisé lorsque le fichier est exécuté directement.

**Exercice 2 :** Utilisez le module `sys` pour récupérer un nom passé en argument dans le terminal et affichez une salutation personnalisée intégrant ce paramètre.


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


# Chapitre 15 : Environnement virtuel adapté à chaque application

La création d'environnements virtuels permet d'isoler les dépendances de chaque application Python pour éviter les conflits entre les bibliothèques installées sur le système. Maîtriser ces outils est indispensable pour garantir la stabilité et la reproductibilité de vos projets.
Dans ce chapitre :

* Création d'un contexte Python isolé avec `venv`
* Utilisation des scripts d'activation et de désactivation (`activate`/`deactivate`)

---

## Création d'un context python isolé avec venv

Le module `venv` permet de générer un répertoire de travail contenant une copie autonome de l'interpréteur Python et de sa bibliothèque standard. Cela isole complètement l'environnement des paquets globaux de la machine.

| Option | Description | Utilisation typique |
| --- | --- | --- |
| **`--clear`** | Supprime le contenu du dossier cible avant de créer le nouvel environnement. | Pour réinitialiser proprement un environnement virtuel existant. |
| **`--upgrade`** | Met à jour le dossier cible pour utiliser la version actuelle de Python tout en conservant les paquets installés. | Après une mise à niveau de la version globale de Python sur la machine. |
| **`--upgrade-deps`** | Met à jour automatiquement `pip` et `setuptools` vers la dernière version disponible lors de la création. | Pour avoir les outils d'installation à jour d'entrée de jeu. |


```bash
# Création d'un environnement virtuel nommé .venv dans le répertoire du projet
python -m venv .venv

```

> 💡 Nommez généralement votre environnement virtuel `.venv` pour qu'il soit facilement identifiable et ignoré par les outils de gestion de versions comme Git.

---

## Script activate/deactivate

Les scripts `activate` et `deactivate` permettent respectivement d'activer et de quitter l'environnement virtuel pour rediriger dynamiquement l'utilisation de la commande `pip` vers le dossier isolé.

```bash
# Activation de l'environnement virtuel sous Linux / macOS
source .venv/bin/activate

```

> 💡 Vérifiez toujours que votre invite de commande affiche le nom de l'environnement entre parenthèses (par exemple `(.venv)`) pour confirmer son activation correcte avant d'installer vos paquets.

---

## Synthèse du chapitre

```bash
# Séquence complète de commandes pour configurer et utiliser un environnement virtuel sous Linux/macOS :

# Création du contexte Python isolé
python -m venv mon_env

# Activation de l'environnement virtuel
source mon_env/bin/activate

# Installation d'une bibliothèque tierce dans cet environnement isolé
pip install requests

# Sortie de l'environnement virtuel
deactivate

```

## Exercices de fin de chapitre

**Exercice 1 :** Exécutez la commande dans votre terminal pour créer un environnement virtuel nommé `env_projet` à la racine de votre dossier de travail.

**Exercice 2 :** Activez l'environnement virtuel créé, vérifiez son bon fonctionnement, puis désactivez-le à l'aide de la commande appropriée.


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

## Gestion des répertoires - mkdir, listdir, move, rmdir

Le module `os` et l'utilitaire `shutil` permettent de manipuler l'arborescence des dossiers. Vous pouvez créer, lister, parcourir récursivement ou supprimer des répertoires. Ces fonctions sont essentielles pour l'automatisation des tâches d'administration système.

```python
import os
import shutil
from pathlib import Path

# Créer des répertoires imbriqués - définition d'un chemin imbriqué
dossier = Path("projets/2026/fichiers_texte")
# Création de l'arborescence complète
dossier.mkdir(parents=True, exist_ok=True)
print(f"Dossier créé : {dossier.resolve()}")

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


# Chapitre 17 : Programmation orientée objets

La programmation orientée objets permet de structurer un programme autour de concepts et de données modélisés sous forme de classes et d'objets. Maîtriser ces principes est indispensable pour concevoir des architectures logicielles modulaires et maintenables.
Dans ce chapitre :

* Approche de l'orienté objets
* Objets et instances de classe (`self`, `super`)
* Composition d'une classe (constructeur, méthodes et données)
* Composition d'une classe - setter, getter
* Héritage de classes et chaînage des constructeurs
* Héritage de classes et redéfinition
* Packages, imports et classes

---
## Approche de l'orienté objets

L'approche orientée objets consiste à regrouper au sein d'une même entité (la classe) les données (attributs) et les traitements (méthodes) qui leur sont associés. Cela favorise l'encapsulation et la réutilisabilité du code. L'orienté objet permet de modéliser les entités métiers observées.

Les piliers de la Programmation Orientée Objet (suite)**

* **Classe :** C'est la structure fondamentale utilisée pour **encapsuler les données** (les attributs) et **les traitements** (les méthodes) associés à une même entité observée. Elle agit comme un modèle ou un plan de fabrication abstract pour tous les éléments de même nature.
* **Objet :** C'est une **instance concrète** d'une classe. À partir d'un seul plan (la classe), on peut instancier un nombre illimité d'objets distincts, chacun possédant son propre état (ses propres valeurs pour chaque attribut) tout en partageant les mêmes comportements (les méthodes).
* **Le Constructeur (`__init__`) :** Il s'agit d'une méthode spéciale exécutée **automatiquement** lors de la création de chaque objet. Son rôle principal est d'initialiser l'état initial de l'instance en lui attribuant ses valeurs de départ.
* **Le paramètre `self` :** En Python, `self` représente une **référence explicite à l'instance courante** de l'objet en cours de manipulation. Il doit être passé comme premier paramètre de toute méthode d'instance afin de pouvoir lire ou modifier les attributs propres à cet objet.
* **L'Encapsulation :** Ce principe consiste à **masquer les détails internes** d'un objet et à protéger ses données contre des modifications directes et involontaires. En Python, la protection se fait par convention d'écriture :
* Un préfixe simple `_attribut` indique un attribut **protégé** (déconseillé à l'accès direct hors de la classe).
* Un préfixe double `__attribut` active le *Name Mangling* (masquage de nom) pour rendre l'attribut **privé**.

* **L'Héritage :** C'est le mécanisme permettant à une classe dite "fille" d'**hériter des propriétés et des méthodes** d'une classe dite "mère". Cela favorise la réutilisation du code et permet d'exprimer des relations hiérarchiques (ex. *Un Chien "est un" Animal*).
* **Le Polymorphisme :** Il permet à des objets issus de classes différentes de proposer une méthode portant le même nom, mais adaptant son comportement selon la classe concernée. Cela permet de traiter différents types d'objets de manière uniforme via une interface commune.

```python
class Vehicule:  # Classe
    def __init__(self, marque: str):  # Constructeur + self
        self.marque = marque  # Attribut public
        self._vitesse = 0  # Attribut protégé (encapsulation)

    def accelerer(self):  # Méthode
        self._vitesse += 10

class Voiture(Vehicule):  # Héritage
    def accelerer(self):  # Polymorphisme (comportement spécifique)
        self._vitesse += 20


# Instanciation de plusieurs objets à partir des classes
ma_voiture = Voiture("Peugeot") 
mon_camion = Vehicule("Volvo")

ma_voiture.accelerer() 
mon_camion.accelerer()

```

> 💡 Pensez vos classes comme des plans de construction permettant de donner naissance à des objets autonomes dotés de comportements spécifiques.

---

## Objet et instance de class - self, super

L'instance représente un objet concret issu d'une classe. Le paramètre `self` fait référence à l'instance courante, tandis que `super()` permet d'accéder aux méthodes de la classe parente en cas d'héritage

```python
# Utilisation de self pour lier les données à l'instance
class Chien:
    def __init__(self, nom):
        self.nom = nom
        
    def aboyer(self):
        return f"{self.nom} aboie !"

```

> 💡 Utilisez systématiquement `self` comme premier paramètre de vos méthodes d'instance pour garantir l'accès correct aux attributs propres de l'objet.

---

## Composition d'une classe - constructeur, méthodes et données

Une classe se compose d'un constructeur (la méthode spéciale `__init__`), de données attributaires et de méthodes pour définir les actions que l'objet peut réaliser.

```python
# Définition d'une classe avec constructeur, attributs et méthodes
class CompteBancaire:
    def __init__(self, titulaire: str, solde_initial: float = 0.0):
        # Attributs (données propres à chaque objet)
        self.titulaire = titulaire
        self.solde = solde_initial

    # Méthode pour afficher les informations du compte
    def afficher_solde(self):
        print(f"Compte de {self.titulaire} : {self.solde:.2f} €")

    # Méthode pour créditer le compte (action)
    def deposer(self, montant: float):
        if montant > 0:
            self.solde += montant
            print(f"Dépôt de {montant:.2f} € effectué.")
        else:
            print("Le montant du dépôt doit être positif.")

    # Méthode pour débiter le compte (action)
    def retirer(self, montant: float):
        if 0 < montant <= self.solde:
            self.solde -= montant
            print(f"Retrait de {montant:.2f} € effectué.")
        else:
            print("Fonds insuffisants ou montant invalide.")

# --- Utilisation de la classe (Instanciation et appel des méthodes) ---

# Instanciation de deux comptes distincts
compte_alice = CompteBancaire("Alice", 1500.0)
compte_bob = CompteBancaire("Bob", 200.0)

# Manipulation des objets
compte_alice.afficher_solde()  # Compte de Alice : 1500.00 €
compte_alice.retirer(500.0)    # Retrait de 500.00 € effectué.
compte_alice.afficher_solde()  # Compte de Alice : 1000.00 €

compte_bob.deposer(150.0)      # Dépôt de 150.00 € effectué.
compte_bob.afficher_solde()    # Compte de Bob : 350.00 €

```
* **Le constructeur (`__init__`) :** initialise les deux attributs (`titulaire` et `solde`) dès la création de l'objet.
* **Les attributs (`self.titulaire`, `self.solde`) :** stockent l'état interne de chaque compte de façon indépendante.
* **Les méthodes (`deposer`, `retirer`, `afficher_solde`) :** contiennent la logique métier pour modifier ou consulter l'état du compte.
> 💡 Le constructeur s'exécute automatiquement lors de l'instanciation de la classe pour initialiser l'état initial des données de l'objet.

---

## Composition d'une classe - setter, getter
L'**encapsulation** consiste à protéger les données d'un objet en empêchant leur modification directe depuis l'extérieur de la classe. Pour consulter ou modifier ces données de façon sécurisée, on utilise des accesseurs (*getters*) et des mutateurs (*setters*).

En Python, la manière la plus élégante et "pythonique" de gérer les *getters* et *setters* repose sur le décorateur **`@property`**. Il permet d'accéder aux attributs comme s'il s'agissait de simples variables, tout en exécutant du code de validation en arrière-plan.

```python
class CompteBancaire:
    def __init__(self, titulaire: str, solde_initial: float = 0.0):
        self.titulaire = titulaire
        self._solde = solde_initial  # Attribut protégé (convention avec '_')

    # GETTER : Permet de lire le solde
    @property
    def solde(self) -> float:
        return self._solde

    # SETTER : Permet de modifier le solde avec un contrôle d'erreur
    @solde.setter
    def solde(self, nouveau_solde: float):
        if nouveau_solde >= 0:
            self._solde = nouveau_solde
        else:
            raise ValueError("Le solde ne peut pas être négatif !")


# --- Utilisation ---

compte = CompteBancaire("Alice", 1000.0)

# Utilisation du GETTER (pas de parenthèses)
print(f"Solde actuel : {compte.solde} €")  # Affiche: 1000.0 €

# Utilisation du SETTER (affectation classique)
compte.solde = 1500.0  # Le contrôle passe par la méthode @solde.setter
print(f"Nouveau solde : {compte.solde} €")  # Affiche: 1500.0 €

# Tentative de modification invalide
try:
    compte.solde = -500.0  # Déclenche l'exception ValueError
except ValueError as e:
    print(f"Erreur : {e}")

```

---

* **Contrôle et sécurité :** Le *setter* permet de valider les données (ex. refuser des valeurs négatives ou de mauvais types) avant de modifier l'état de l'objet.
* **Accès transparent :** Grâce à `@property`, l'utilisateur de la classe lit et modifie l'attribut avec une syntaxe naturelle (`compte.solde = 500`) sans savoir qu'une méthode de contrôle est exécutée.
* **Convention d'encapsulation :** L'attribut réel est préfixé d'un tiret bas (`_solde`) pour signaler qu'il s'agit d'une donnée interne ne devant pas être manipulée directement.
* 
## Héritage de classes et chaînage des constructeurs

L'**héritage** permet à une classe fille (ou dérivée) d'accéder aux attributs et méthodes d'une classe mère (ou parente). Le **chaînage des constructeurs** consiste à appeler le constructeur de la classe mère depuis le constructeur de la classe fille à l'aide de la fonction intégrée `super()`. Cela garantit que la partie "parente" de l'objet est correctement initialisée avant d'y ajouter les spécificités de la classe fille.

```python
# Classe mère (Parente)
class CompteBancaire:
    def __init__(self, titulaire: str, solde_initial: float = 0.0):
        self.titulaire = titulaire
        self.solde = solde_initial

    def afficher_solde(self):
        print(f"Compte de {self.titulaire} : {self.solde:.2f} €")

    def deposer(self, montant: float):
        if montant > 0:
            self.solde += montant


# Classe fille (Hérite de CompteBancaire)
class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire: str, solde_initial: float = 0.0, taux_interet: float = 0.02):
        # Chaînage du constructeur : appel du __init__ de CompteBancaire
        super().__init__(titulaire, solde_initial)
        
        # Attribut spécifique à la classe fille
        self.taux_interet = taux_interet

    # Méthode propre à la classe fille
    def ajouter_interets(self):
        interets = self.solde * self.taux_interet
        self.solde += interets
        print(f"Intérêts ajoutés ({self.taux_interet * 100}%) : +{interets:.2f} €")


# --- Utilisation ---

# Création d'une instance de la classe fille
mon_epargne = CompteEpargne("Charlie", 1000.0, taux_interet=0.03)

# Utilisation des méthodes héritées
mon_epargne.afficher_solde()  # Compte de Charlie : 1000.00 €
mon_epargne.deposer(500.0)

# Utilisation des fonctionnalités propres à CompteEpargne
mon_epargne.ajouter_interets() # Intérêts ajoutés (3.0%) : +45.00 €
mon_epargne.afficher_solde()  # Compte de Charlie : 1545.00 €

```

---

* **Syntaxe de l'héritage :** `class ClasseFille(ClasseMere):` déclare la relation de parenté.
* **Fonction `super()` :** renvoie une référence temporaire à la classe mère pour invoquer sa méthode `__init__()` ou d'autres méthodes surchargées.
* **Réutilisation de code :** la classe fille hérite automatiquement de toutes les méthodes publiques (`deposer`, `afficher_solde`) sans avoir à les réécrire.


## Héritage de classes et redéfinition

L'héritage permet de créer une nouvelle classe (fille) à partir d'une classe existante (parente) pour réutiliser du code et redéfinir certains comportements spécifiques.

```python
# Héritage simple et spécialisation
class Animal:
    def emettre_son(self):
        return "Son générique"

class Chat(Animal):
    def emettre_son(self):
        return "Miaou"

```

> 💡 La redéfinition de méthodes (*method overriding*) permet d'adapter le comportement d'une classe fille tout en conservant la signature de la classe parente.

---

## Packages et imports et classes

L'organisation des classes au sein de modules et de packages permet de structurer les grands projets logiciels et de les importer proprement là où ils sont nécessaires.

```python
# Importation ciblée d'une classe depuis un module de package
# from mon_package.modele import CompteBancaire

```

> 💡 Veillez à regrouper les classes ayant des responsabilités métiers proches au sein d'un même module pour préserver la clarté de votre architecture.

---

## Exemple de synthèse

```python
# Programme complet combinant classes, constructeur, méthodes, self, héritage et redéfinition

class Utilisateur:
    """Classe parente représentant un utilisateur générique."""
    def __init__(self, identifiant):
        self.identifiant = identifiant

    def obtenir_profil(self):
        return f"Utilisateur ID : {self.identifiant}"

class Administrateur(Utilisateur):
    """Classe fille héritant d'Utilisateur avec redéfinition."""
    def __init__(self, identifiant, niveau_acces):
        super().__init__(identifiant)  # Appel du constructeur parent
        self.niveau_acces = niveau_acces

    def obtenir_profil(self):
        # Redéfinition de la méthode héritée
        profil_base = super().obtenir_profil()
        return f"{profil_base} | Rôle : Admin (Niveau {self.niveau_acces})"

# Instanciation et test des objets
admin = Administrateur("USR-001", 3)
print(admin.obtenir_profil())

```

## Exercices de fin de chapitre

**Exercice 1 :** Créez une classe `Livre` possédant un constructeur initialisant un titre et un auteur, ainsi qu'une méthode retournant une description textuelle de l'ouvrage.

**Exercice 2 :** Développez une classe fille `LivreNumerique` qui hérite de la classe `Livre` en y ajoutant un attribut supplémentaire pour la taille du fichier en mégaoctets, puis instanciez un objet de cette classe.


# Chapitre 18 : La programmation asynchrone avec `asyncio`

La gestion efficace des opérations d'entrée/sortie (E/S) — comme l'accès au réseau, aux bases de données ou au système de fichiers — est cruciale pour concevoir des applications Python performantes. Dans ce chapitre, vous découvrirez les principes de la programmation asynchrone non bloquante. Vous apprendrez à utiliser le module standard `asyncio` pour exécuter plusieurs tâches de manière concurrente sans avoir recours au multithreading complexe.

* Les différences fondamentales entre l'exécution synchrone bloquante et asynchrone non bloquante
* Les coroutines, les objets `Future`/`Task` et la syntaxe `async` / `await`
* Le rôle essentiel de la boucle d'événements (*event loop*)
* La planification et le regroupement de tâches concurrentes avec `asyncio.gather()` et `asyncio.TaskGroup`

---

## Appels non bloquants et concurrents

En programmation synchrone (classique), lorsqu'un programme effectue une opération d'E/S (comme télécharger une page web), le fil d'exécution reste bloqué en attendant la réponse. Durant cet intervalle, le processeur ne traite aucune autre instruction.

L'approche **asynchrone et non bloquante** permet de libérer le fil d'exécution pendant ces temps d'attente : dès qu'une tâche s'interrompt pour attendre un résultat externe, le programme passe immédiatement à l'exécution d'une autre tâche.

```python
import time

# Exemple synchrone (bloquant) : les tâches s'exécutent en séquence
def tache_synchrone(nom, duree):
    print(f"Début de la tâche {nom}")
    time.sleep(duree)  # Bloque tout le programme pendant 'duree' secondes
    print(f"Fin de la tâche {nom}")

tache_synchrone("A", 2)
tache_synchrone("B", 1)
# Temps total d'exécution : 3 secondes

```

> 💡 **Note**
> La concurrence n'est pas le parallélisme. La concurrence gère plusieurs tâches en alternance sur un seul thread (idéal pour les opérations dépendantes du réseau/E/S), tandis que le parallélisme exécute plusieurs calculs simultanément sur plusieurs cœurs processeur (idéal pour les calculs intenses).

---

## Promise ou Future avec async, await

En Python, une fonction asynchrone se définit avec le mot-clé `async def` et produit une **coroutine**. Pour suspendre l'exécution d'une coroutine et céder le contrôle au moteur asynchrone, on utilise le mot-clé `await`.

Les objets sous-jacents gérant ces opérations différées s'appellent des **Futures** (ou **Tasks** quand ils enveloppent une coroutine). Une *Future* représente un résultat qui n'est pas encore disponible, mais qui le sera plus tard.

```python
import asyncio

async def telecharger_donnees(id_requete):
    print(f"Ressource {id_requete} : téléchargement démarré...")
    # asyncio.sleep simule une attente I/O non bloquante
    await asyncio.sleep(2)
    print(f"Ressource {id_requete} : téléchargement terminé.")
    return {"id": id_requete, "statut": "OK"}

async def main():
    # 'await' attend la résolution de la coroutine sans bloquer le reste de la boucle
    resultat = await telecharger_donnees(101)
    print("Résultat obtenu :", resultat)

# Exécution de la coroutine principale
asyncio.run(main())

```

> ⚠️ **Piège**
> N'utilisez jamais `time.sleep()` à l'intérieur d'une coroutine asynchrone. Cela bloquerait la boucle d'événements tout entière. Utilisez toujours sa variante asynchrone : `await asyncio.sleep()`.

---

## La boucle d'événements (`event loop`)

La **boucle d'événements** (*event loop*) est le cœur réactif du système `asyncio`. Elle maintient la liste de toutes les tâches en cours, surveille leur état (en attente, prêtes, terminées) et distribue le temps de processeur au fur et à mesure que les événements se produisent.

Depuis Python 3.7, la fonction `asyncio.run()` gère automatiquement la création, l'exécution et la fermeture propre de la boucle d'événements.

```python
import asyncio

async def notifier_utilisateur():
    print("Notification envoyée à l'utilisateur.")

async def main():
    # Obtenir la référence de la boucle d'événements courante
    loop = asyncio.get_running_loop()
    print(f"Boucle d'événements active : {loop}")
    
    # Création d'une tâche explicite liée à la boucle
    tache = loop.create_task(notifier_utilisateur())
    await tache

# asyncio.run() initialise et ferme la boucle automatiquement
asyncio.run(main())

```

> Privilégiez l'utilisation de `asyncio.run(main())` comme point d'entrée de votre application au lieu de manipuler directement la boucle avec `get_event_loop()` ou `loop.run_until_complete()`.

---

## Gestion des tâches concurrentes

Pour tirer le plein potentiel de l'asynchronisme, il est essentiel d'exécuter plusieurs coroutines en parallèle. `asyncio` propose plusieurs mécanismes pour orchestrer et regrouper ces tâches.

**Utilisation de `asyncio.gather()`**

`asyncio.gather()` permet de lancer plusieurs coroutines simultanément et de collecter leurs résultats dans une liste ordonnée.

```python
import asyncio
import time

async def traiter_commande(id_commande, delai):
    await asyncio.sleep(delai)
    return f"Commande {id_commande} traitée en {delai}s"

async def main():
    debut = time.perf_counter()
    
    # Lancement concurrent de 3 commandes
    resultats = await asyncio.gather(
        traiter_commande(1, 2),
        traiter_commande(2, 1),
        traiter_commande(3, 3)
    )
    
    fin = time.perf_counter()
    print("Résultats :", resultats)
    print(f"Temps total d'exécution : {fin - debut:.2f} secondes")

asyncio.run(main())

```

Pour exécuter ce script depuis votre terminal :

```bash
python script_async.py

```

**Utilisation moderne avec `asyncio.TaskGroup`**

À partir de Python 3.11, l'utilisation de `asyncio.TaskGroup` est recommandée pour une gestion plus sûre des exceptions (gestion contextuelle d'erreurs concurrentes via les *Exception Groups*).

```python
import asyncio

async def service_a():
    await asyncio.sleep(1)
    print("Service A prêt")

async def service_b():
    await asyncio.sleep(1.5)
    print("Service B prêt")

async def main():
    # Le bloc TaskGroup garantit que toutes les tâches terminent ou sont annulées proprement en cas d'erreur
    async with asyncio.TaskGroup() as tg:
        tg.create_task(service_a())
        tg.create_task(service_b())
    
    print("Tous les services sont opérationnels.")

asyncio.run(main())

```

---

## Exercices de fin de chapitre

Dans ce chapitre, vous avez découvert les mécanismes de l'exécution asynchrone en Python grâce au module `asyncio`. Vous avez appris à définir des coroutines avec `async` et `await`, à planifier leur exécution au sein de la boucle d'événements, ainsi qu'à gérer plusieurs appels non bloquants en parallèle à l'aide de `asyncio.gather` et `TaskGroup`.

**Exercice 1 : traitement concurents**
Créez deux coroutines t1() et t2() qui simulent un traitement en attendant des durées différentes (ex: 1s et 3s avec asyncio.sleep).
Chaque coroutine doit afficher un message d'exécution et retourner la chaîne "fin de traitement".
Exécutez-les de manière concurrente avec asyncio.gather() puis affichez leurs valeurs de retour.

**Exercice 2 : traitement concurents avec une exception de délai dépassé, exception asyncio.TimeoutError**
Reprenez les coroutines t1() et t2() de l'exercice précédent.
Exécutez la tâche la plus longue en la limitant avec asyncio.wait_for(..., timeout=2.0).
Interceptez l'exception asyncio.TimeoutError à l'aide d'un bloc try/except pour afficher un message d'erreur lorsque le délai maximal est dépassé.


# Chapitre 19 : Accès aux bases de données

L'accès aux bases de données permet de persister, d'interroger et de structurer des volumes importants d'informations de manière sécurisée en Python. Maîtriser ces concepts est indispensable pour connecter vos applications à des systèmes de stockage relationnels.
Dans ce chapitre :

* Concepts de base des bases de données relationnelles
* Connexion et paramétrage via la connexion et le curseur
* Gestion de la Structure de données - requêtes DDL
* Manipulation des données - requêtes DML
* Gestion des transactions — commit et rollback
* Bonne pratique : Gestion sécurisée des connexions

---

## Concepts de base

Les bases de données relationnelles (SGBDR) permettent de stocker et d'organiser des données tabulaires structurées sous forme de **tables** composées de **lignes** (enregistrements ou n-uplets) et de **colonnes** (attributs ou champs).

Grâce aux contraintes d'intégrité et au respect des propriétés ACID (Atomicité, Cohérence, Isolation, Durabilité), elles garantissent la **cohérence des données**, la **rapidité de recherche** via des indexations optimisées et la **gestion de la concurrence d'accès** simultanée par plusieurs utilisateurs.

---

**Concepts clés**

* **Table (ou Relation) :** Structure bidimensionnelle représentant une entité du monde réel (ex. `Client`, `Commande`).
* **Clé primaire (*Primary Key*) :** Attribut unique (ex. un identifiant ou un code) permettant de distinguer chaque ligne d'une table sans ambiguïté.
* **Clé étrangère (*Foreign Key*) :** Attribut établissant un lien relationnel entre deux tables en référençant la clé primaire d'une autre table.
* **Langage SQL (*Structured Query Language*) :** Langage standardisé utilisé pour interroger et manipuler les données (via les commandes `SELECT`, `INSERT`, `UPDATE`, `DELETE`).

---

## Connexion et paramétrage - connexion, cursor

La connexion établit le pont entre l'application Python et le fichier ou serveur de base de données, tandis que le curseur sert d'intermédiaire pour exécuter les requêtes SQL.

En Python, la norme **DB-API 2.0** définit une interface standardisée pour interagir avec les bases de données. Le module intégré **`sqlite3`** permet d'exploiter une base de données relationnelle légère et serveur-less sans nécessiter de configuration externe complexifiée.

```python
import sqlite3

# Connexion à la base de données (fichier local ou en mémoire via ':memory:')
connexion = sqlite3.connect("ma_banque.db")

# Création d'un curseur pour exécuter les requêtes SQL
curseur = connexion.cursor()

# Création d'une table avec clés et contraintes
curseur.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

```

> 💡 Pensez toujours à fermer explicitement votre curseur et votre connexion à la fin des traitements pour libérer les ressources système verrouillées.

---

## Gestion de la Structure de données - requêtes DDL

Le langage de définition de données (DDL) permet de créer, modifier ou supprimer la structure des tables au sein de la base de données (instructions `CREATE TABLE`, etc.).

Les opérations qui portent sur la structure des tables sont : DDL (CREATE, ALTER, DROP, TRUNCATE) 

```python
# Création d'une table relationnelle via une requête DDL
curseur.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        age INTEGER
    )
""")

```

> 💡 Définissez rigoureusement les types de données et les contraintes (`NOT NULL`, `PRIMARY KEY`) dès la conception de vos tables pour garantir l'intégrité des informations.

---

## Manipulation des données - requêtes DML

Le langage de manipulation des données (DML) permet d'insérer, de modifier, de supprimer et de rechercher des enregistrements à l'aide des instructions `SELECT` et de la clause `WHERE`.

Les opérations qui portent sur les données des tables sont : DML (SELECT, INSERT, UPDATE, DELETE) 

Voici plusieurs exemples concrets d'opérations **DML** (*Data Manipulation Language*) en Python avec `sqlite3`, illustrant les différentes façons d'insérer, lire, mettre à jour et supprimer des données.

---

**Insertion d'une seule ligne**

```python
# Insertion simple avec passage de paramètres sous forme de tuple
nouvel_utilisateur = ("Alice", 25, "alice@example.com")
curseur.execute(
    "INSERT INTO utilisateurs (nom, age, email) VALUES (?, ?, ?)",
    nouvel_utilisateur
)
connexion.commit()

```

**Insertion multiple en masse (`executemany`)**

```python
# Liste de tuples pour insérer plusieurs lignes en une seule opération
plusieurs_utilisateurs = [
    ("Bob", 17, "bob@example.com"),
    ("Charlie", 30, "charlie@example.com"),
    ("Diana", 22, "diana@example.com")
]
curseur.executemany(
    "INSERT INTO utilisateurs (nom, age, email) VALUES (?, ?, ?)",
    plusieurs_utilisateurs
)
connexion.commit()

```

---

**Récupérer un seul enregistrement (`fetchone`)**

```python
# Utile quand on recherche par identifiant unique ou clé primaire
curseur.execute("SELECT * FROM utilisateurs WHERE email = ?", ("alice@example.com",))
utilisateur = curseur.fetchone()

if utilisateur:
    print(f"Trouvé : {utilisateur}")  # Retourne un tuple : (1, 'Alice', 25, 'alice@example.com')

```

**Récupérer un nombre limité d'enregistrements (`fetchmany`)**

```python
# Récupère uniquement les 2 premiers résultats
curseur.execute("SELECT nom, age FROM utilisateurs ORDER BY age DESC")
top_2 = curseur.fetchmany(2)
print("Les 2 plus âgés :", top_2)

```

**Filtrage complexe avec tris et limites**

```python
# Recherche multi-critères
sql = """
SELECT nom, age 
FROM utilisateurs 
WHERE age >= ? AND nom LIKE ? 
ORDER BY nom ASC 
LIMIT ?
"""
curseur.execute(sql, (18, "A%", 10))  # Majeurs dont le nom commence par 'A', max 10
resultats = curseur.fetchall()

```

---

**Modification de données (`UPDATE`)**

```python
# Mise à jour du champ 'age' pour un utilisateur spécifique
nouvel_age = 26
email_cible = "alice@example.com"

curseur.execute(
    "UPDATE utilisateurs SET age = ? WHERE email = ?",
    (nouvel_age, email_cible)
)
connexion.commit()

# Afficher le nombre de lignes modifiées
print(f"Lignes modifiées : {curseur.rowcount}")

```

---

**Suppression de données (`DELETE`)**

```python
# Suppression des utilisateurs mineurs
age_limite = 18

curseur.execute("DELETE FROM utilisateurs WHERE age < ?", (age_limite,))
connexion.commit()

print(f"Utilisateurs supprimés : {curseur.rowcount}")

```

---

**Synthèse des méthodes de récupération (`fetch`)**

| Méthode | Comportement | Retour si aucun résultat |
| --- | --- | --- |
| **`curseur.fetchone()`** | Retourne la **première ligne** sous forme de tuple. | `None` |
| **`curseur.fetchall()`** | Retourne **toutes les lignes** sous forme d'une liste de tuples. | `[]` *(liste vide)* |
| **`curseur.fetchmany(size)`** | Retourne **au maximum `size` lignes** sous forme de liste. | `[]` *(liste vide)* |

> 💡 Utilisez toujours des requêtes paramétrées (avec des points d'interrogation `?`) pour injecter des variables afin de vous prémunir totalement contre les failles d'injection SQL.

---
## Gestion des transactions — commit et rollback

La gestion des transactions permet de valider définitivement un ensemble d'opérations en base de données grâce à l'instruction `commit`, garantissant la cohérence globale des données.

```python
import sqlite3

connexion = sqlite3.connect("banque.db")
curseur = connexion.cursor()

# Exemple de transfert d'argent entre deux comptes (Opération atomique)
compte_source = 1
compte_dest = 2
montant = 150.0

try:
    # 1. Débit du compte source
    curseur.execute(
        "UPDATE comptes SET solde = solde - ? WHERE id = ?",
        (montant, compte_source)
    )

    # 2. Crédit du compte destinataire
    curseur.execute(
        "UPDATE comptes SET solde = solde + ? WHERE id = ?",
        (montant, compte_dest)
    )

    # Validation définitive de l'ensemble des modifications
    connexion.commit()
    print("Transaction réussie et validée en base de données.")

except sqlite3.Error as e:
    # En cas d'erreur SQL, annulation de TOUTES les modifications de la transaction
    connexion.rollback()
    print(f"Erreur lors de la transaction. Modifications annulées : {e}")

finally:
    connexion.close()

```

> 💡 En cas d'erreur lors d'une transaction, utilisez l'instruction `rollback` pour annuler les modifications en cours et rétablir l'état stable précédent de la base.

---
--- 
## Bonne pratique : Gestion sécurisée des connexions

Pour éviter les fuites de mémoire et garantir la fermeture automatique des ressources même en cas d'erreur, utilisez un gestionnaire de contexte (`with`) :

```python
import sqlite3

# Le gestionnaire de contexte gère le commit/rollback automatiquement
with sqlite3.connect("ma_banque.db") as connexion:
    curseur = connexion.cursor()
    curseur.execute("SELECT COUNT(*) FROM clients")
    total = curseur.fetchone()[0]
    print(f"Nombre total de clients : {total}")
# La connexion se ferme proprement en sortant du bloc with

```
---

**Alternative moderne : Le gestionnaire de contexte (`with`)**

En Python, le gestionnaire de contexte gère les transactions automatiquement : il effectue un `commit()` si le bloc s'exécute sans erreur, ou un `rollback()` si une exception est levée.

```python
import sqlite3

connexion = sqlite3.connect("banque.db")

# Le bloc 'with connexion:' gère automatiquement la transaction (commit/rollback)
try:
    with connexion:
        connexion.execute("UPDATE comptes SET solde = solde - 100 WHERE id = 1")
        connexion.execute("UPDATE comptes SET solde = solde + 100 WHERE id = 2")
    print("Transaction validée automatiquement.")
except sqlite3.Error:
    print("Erreur détectée : rollback automatique effectué.")

```
---
---

## Exemple de synthèse

```python
import sqlite3

def gerer_base_de_donnees():
    """Programme complet combinant connexion, DDL, transactions et requêtes DML."""
    # 1. Connexion et paramétrage
    connexion = sqlite3.connect("entreprise.db")
    curseur = connexion.cursor()
    
    # 2. Gestion de la structure de données (DDL)
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS employes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            salaire REAL
        )
    """)
    
    # 3. Insertion de données (DML) et gestion des transactions (commit)
    curseur.execute("INSERT INTO employes (nom, salaire) VALUES (?, ?)", ("Alice", 2500.0))
    curseur.execute("INSERT INTO employes (nom, salaire) VALUES (?, ?)", ("Bob", 3100.0))
    connexion.commit()  # Validation de la transaction
    
    # 4. Manipulation des données avec SELECT et WHERE (DML)
    curseur.execute("SELECT nom, salaire FROM employes WHERE salaire > ?", (2800.0,))
    recrutements_hauts = curseur.fetchall()
    
    for employe in recrutements_hauts:
        print(f"Employé qualifié : {employe[0]} avec un salaire de {employe[1]}€")
        
    # Fermeture propre des ressources
    curseur.close()
    connexion.close()

# Exécution de la fonction de synthèse
gerer_base_de_donnees()

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script Python qui utilise le module `sqlite3` pour créer une base de données, instancier une table `produits` (contenant un ID, un nom et un prix), puis y insérer un enregistrement validé par un `commit`.

**Exercice 2 :** Rédigez une requête `SELECT` associée à une clause `WHERE` pour récupérer et afficher tous les produits dont le prix est inférieur à un certain seuil depuis la table créée à l'exercice précédent.


# Chapitre 20 : Les tests unitaires avec `unittest`

Garantir la fiabilité d'un code avant son déploiement est une étape indispensable du développement logiciel. Dans ce chapitre, vous découvrirez comment concevoir des tests unitaires automatisés pour vérifier le bon fonctionnement de vos fonctions et classes. L'objectif est d'acquérir les réflexes méthodologiques et d'utiliser les outils standards pour livrer des projets Python robustes et maintenables.

* L'intérêt des tests unitaires et les terminologies fondamentales (*assertion*, *fixture*, *suite*)
* L'utilisation du module standard `unittest`
* L'écriture d'une suite de tests complète sur un cas pratique (`Calcul`)
* La mesure de la couverture de code avec l'outil `coverage.py`

---

## Nécessité du test et concepts fondamentaux

Tester un programme permet d'identifier les bugs avant la mise en production et d'éviter les régressions lors de l'ajout de nouvelles fonctionnalités. Un **test unitaire** isole la plus petite unité de code possible (généralement une fonction ou une méthode) pour en vérifier le comportement face à des entrées données.

Plusieurs concepts clés structurent l'écriture des tests :

* **Assertion** : une vérification logique qui valide si le résultat obtenu correspond au résultat attendu.
* **Fixture** : la mise en place d'un environnement contrôlé (variables, instances, connexions) avant l'exécution du test, puis son nettoyage après.
* **Suite de tests** : un regroupement de plusieurs cas de tests exécutés ensemble.

```python
# Exemple d'assertion basique en Python pur sans framework
def additionner(a, b):
    return a + b

# Vérification manuelle (lève une AssertionError si le résultat est incorrect)
assert additionner(2, 3) == 5, "L'addition de 2 et 3 doit valoir 5"

```

> Un bon test unitaire doit être **I.S.O.L.É.** : Indépendant, Saisissable (lisible), Automatique, Répétable et Rapide. Un test ne doit jamais dépendre de l'exécution d'un autre test.

---

## Prise en main du framework standard `unittest`

Python intègre nativement le module `unittest`, inspiré du framework *JUnit*. Il fournit une structure orientée objet basée sur la classe `unittest.TestCase`.

Pour créer un cas de test, il suffit de dériver de `unittest.TestCase` et de concevoir des méthodes dont le nom commence obligatoirement par le préfixe `test_`.

Module à tester : parite.py
```python
def est_pair(nombre):
    """Retourne True si le nombre est pair, False sinon."""
    return nombre % 2 == 0
```

Module de teste : parite.test.py
```python
import unittest

# TestEstPair prend ses fonctionnalités oar héritage de unittest.TestCase
class TestEstPair(unittest.TestCase):

	# obligation de prefixer avec test_<nom methode>
    def test_nombre_pair(self):
        self.assertTrue(est_pair(4))

	# obligation de prefixer avec test_<nom methode>
    def test_nombre_impair(self):
        self.assertFalse(est_pair(7))

if __name__ == '__main__':
    unittest.main()

```

Il y a une grande librairies d'assertion mais voici les plus fréquentes fournies par `unittest.TestCase`:

* `assertEqual(a, b)` : vérifie que `a == b`
* `assertNotEqual(a, b)` : vérifie que `a != b`
* `assertTrue(x)` / `assertFalse(x)` : vérifie l'état booléen de `x`
* `assertRaises(Exception)` : vérifie qu'une exception spécifique est bien levée

---

## tester la classe Calcul

Appliquons la démarche sur une classe métier `Calcul` gérant des opérations arithmétiques et des cas limites (division par zéro).

**Implémentation de la classe à tester**

```python
# fichier: calcul.py

class Calcul:
    """Classe fournissant des opérations mathématiques de base."""
    
    def additionner(self, a, b):
        return a + b

    def diviser(self, a, b):
        if b == 0:
            raise ValueError("La division par zéro est impossible.")
        return a / b

```

**Écriture du fichier de test**

Nous utilisons `setUp()` pour instancier la classe `Calcul` avant chaque test.

```python
# fichier: test_calcul.py
import unittest
from calcul import Calcul

class TestCalcul(unittest.TestCase):

    def setUp(self):
        """Fixture : exécutée automatiquement avant chaque méthode de test."""
        self.calculateur = Calcul()

    def test_additionner(self):
        resultat = self.calculateur.additionner(10, 5)
        self.assertEqual(resultat, 15)

    def test_diviser_valeurs_valides(self):
        resultat = self.calculateur.diviser(10, 2)
        self.assertEqual(resultat, 5.0)

    def test_diviser_par_zero(self):
        """Vérifie que la division par zéro lève bien une ValueError."""
        with self.assertRaises(ValueError):
            self.calculateur.diviser(10, 0)

if __name__ == '__main__':
    unittest.main()

```

**Pour exécuter cette suite de tests depuis votre terminal **

```bash
python -m unittest test_calcul.py

```


> ⚠️ **Piège**
> N'oubliez pas le préfixe `test_` devant le nom de vos méthodes dans la classe de test. Tout méthode sans ce préfixe sera ignorée par le moteur de `unittest`.

---

## Mesure de la couverture de code (*Code Coverage*)

La **couverture de code** mesure le pourcentage de lignes de code métier exécutées lors du lancement des tests unitaires. Elle permet de repérer les zones de code oubliées ou non testées (comme des branches conditionnelles `if/else` spécifiques).

En Python, l'outil le plus répandu est la bibliothèque `coverage`.

## Installation et utilisation

**Installation via pip :**

```bash
pip install coverage

```

**Exécution des tests sous le contrôle de coverage :**

```bash
coverage run -m unittest test_calcul.py

```

**Affichage du rapport dans la console :**

```bash
coverage report -m

```

L'option `-m` (missing) indique les numéros des lignes qui n'ont pas été couvertes lors des tests.

**Génération d'un rapport HTML détaillé :**

```bash
coverage html

```

Cette commande crée un dossier `htmlcov/` contenant une interface web permettant de visualiser ligne par ligne le code couvert et non couvert.

> 💡 **Note**
> Viser 100 % de couverture est une bonne ambition, mais une couverture élevée ne garantit pas l'absence totale de bugs. La qualité des jeux de données et des assertions reste prédominante.

---

## Exercices de fin de chapitre

Dans ce chapitre, vous avez appris à structurer vos tests unitaires grâce au module `unittest`, à automatiser la vérification de vos fonctions et à valider la levée d'exceptions. Vous avez également vu comment quantifier l'efficacité de votre suite de tests avec l'outil de métrique `coverage.py`.

**Exercice 1 : teste une fonction `def aleatoire`**
Pour une fonction aleatoire basée sur random.randint(), valider le fait que sur 100 tirages de valeurs comprises dans l'interval [0,20], il y a autant de valeur paires que de valeur impairs

**Exercice 2 : teste une dans une `class Aleatoire`**
Pour une classe contenant la fonction aleatoire basée sur random.randint(), valider le fait que sur 100 tirages de valeurs comprises dans l'interval [0,20], il y a autant de valeur paires que de valeur impairs
Générez le rapport `coverage` pour vérifier que 100 % de la classe `Aleatoire` est couverte.


# L'essentiel de l'essentiel à retenir sur Python

## Installation & commandes

```bash
python --version                     # vérifier la version de Python
python -m venv .venv                 # créer un environnement virtuel
source .venv/bin/activate            # activer venv (Linux/macOS)
.venv\Scripts\activate               # activer venv (Windows)
deactivate                           # désactiver l'environnement virtuel
pip install package                  # installer un paquet
pip freeze > requirements.txt        # geler les dépendances
pip install -r requirements.txt      # installer les dépendances
python main.py                       # exécuter un script Python
python -m pytest                     # exécuter les tests unitaires
python -m pytest --cov               # couverture de code

```

## Variables & types scalaires

```python
# Affectation dynamique
x = 1
PI = 3.14

n = 10                               # int
prix = 19.99                         # float
ok = True                            # bool
s = "texte"                          # str
v = None                             # NoneType (absence de valeur)
u = 5                                # union logique (dynamique)

```

## Types agrégés

```python
obj = {"nom": "A", "age": 30}         # dict
arr = [1, 2, 3]                      # list (mutable)
tup = ("a", 1)                       # tuple (immuable)
ens = {1, 2, 3}                      # set (éléments uniques)
from enum import Enum
class Couleur(Enum): ROUGE = 1       # enum
opt = None                           # optionnel / nullable
ID = int | str                       # type alias (Python 3.10+)

```

## Casting

```python
v1 = str(125)                        # int -> str ("125")
v2 = int("42")                       # str -> int (42)
v3 = float("19.99")                  # str -> float (19.99)
v4 = list({1, 2, 3})                 # set -> list

```

## Opérateurs

```python
+ - * / // % **                      # arithmétiques (// entière, ** puissance)
== != < > <= >=                      # relationnels
and or not                           # logiques
= += -= *=                           # affectation
x if condition else y                # ternaire
a | b                                # union d'ensembles ou de types

```

## Contrôle de flux

```python
if x > 0: pass
elif x == 0: pass
else: pass

match x:                             # Python 3.10+
    case 1: pass
    case _: pass

for i in range(10): pass
for item in arr: pass
for k, v in obj.items(): pass
while x < 10: pass

```

## Fonctions & arguments

```python
def add(a: int, b: int) -> int: return a + b
def sum_all(*args: int) -> int: return sum(args)           # *args : arguments positionnels variables (tuple)
def config(**kwargs): print(kwargs.get("theme"))          # **kwargs : arguments nommés variables (dict)
def combo(x, *args, **kwargs): pass                        # combinaison classique

mul = lambda a, b: a * b                                   # anonyme / lambda
def identity(val: T) -> T: return val                       # générique
```

## Générateurs 
```python
def compte_jusqua(n: int):
    for i in range(n):
        yield i                                           # produit une valeur et suspend l'exécution

gen = compte_jusqua(5)
next(gen)                                                 # 0 (récupère l'élément suivant)
gen_exp = (x**2 for x in range(10))                        # expression génératrice (analogue aux list comprehension)

```

## Fonctions d'ordre supérieur
```python
list(map(lambda x: x * 2, arr))
list(filter(lambda x: x > 0, arr))
from functools import reduce
reduce(lambda acc, x: acc + x, arr, 0)
```

## Exceptions

```python
try:
    raise ValueError("oups")
except ValueError as e:
    print(e)
finally:
    pass                             # toujours exécuté

```

## Modules & Packages

```python
# mon_module.py
def f(): pass
class C: pass
o = {}

# main.py
from mon_module import f, C, o
import os
from pathlib import Path

```

## Fichiers & Répertoires

```python
# Modes open(): 'r' (lecture), 'w' (écriture/écrasement), 'a' (ajout), 'b' (binaire)

# Lecture / Écriture de texte
with open("fichier.txt", "r", encoding="utf-8") as f:
    texte = f.read()                 # lit tout
    for line in f: pass              # itération ligne par ligne

with open("fichier.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")

# Accès aléatoire (binaire / texte)
with open("data.bin", "rb") as f:
    f.seek(10)                        # déplace le pointeur au 10ème octet
    pos = f.tell()                   # position actuelle du pointeur

# Répertoires & Chemins (pathlib)
from pathlib import Path

p = Path("dossier/sous_dossier/fichier.txt")
p.parent.mkdir(parents=True, exist_ok=True)  # mkdirs (crée parents)
p.exists()                           # vérifie si existe
p.is_file()                          # est un fichier
p.is_dir()                           # est un dossier
content = p.read_text(encoding="utf-8")      # lecture directe
p.write_text("ok", encoding="utf-8")         # écriture directe

```

## POO simple (Bases & Encapsulation)

```python
class CompteBancaire:
    def __init__(self, titulaire: str, solde: float = 0.0):
        self.titulaire = titulaire   # attribut public
        self._solde = solde          # attribut protégé (convention)
        self.__secret = "1234"       # attribut privé (name mangling)

    def deposer(self, montant: float):
        if montant > 0: self._solde += montant

    @property                        # getter
    def solde(self) -> float:
        return self._solde

    @solde.setter                    # setter avec contrôle
    def solde(self, valeur: float):
        if valeur >= 0: self._solde = valeur

    def __str__(self) -> str:        # méthode spéciale (dunder)
        return f"Compte({self.titulaire}, {self._solde}€)"

compte = CompteBancaire("Alice", 100)
compte.deposer(50)
print(compte.solde)                  # appel du getter (150)

```

## POO avancée (Héritage & Abstraction)

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    espece = "inconnue"               # attribut de classe / static
    def __init__(self, nom: str):
        self._nom = nom

    @abstractmethod
    def crier(self): pass

class Chien(Animal):
    def __init__(self, nom: str, race: str):
        super().__init__(nom)        # chaînage des constructeurs
        self.race = race

    def crier(self):                 # polymorphisme
        print(f"{self._nom} aboie")

class Generique[T]:
    def __init__(self, v: T):
        self.valeur = v

```

## Asynchrone

```python
import asyncio

async def attendre(ms: int):
    await asyncio.sleep(ms / 1000)

async def main():
    await attendre(1000)
    print("fait")

# asyncio.run(main())

```

## Tests avec Unittest & Couverture de code (CLI & Code)

```bash
# Commandes Unittest en ligne de commande (CLI)
python -m unittest                          # exécute tous les tests du projet (découverte automatique)
python -m unittest test_script.py           # exécute un fichier de test spécifique
python -m unittest test_script.TestCas.test_add # exécute un test précis (fichier.Classe.methode)
python -m unittest discover -s tests -p "test_*.py" # exécute les tests dans le dossier 'tests'
python -m unittest -v                       # mode verbeux (détaille chaque test)
python -m unittest -f                       # s'arrête au premier échec rencontrée (-f / --failfast)

# Couverture de code avec l'outil natif 'coverage'
coverage run -m unittest                    # exécute les tests unittest et mesure la couverture
coverage run --source=mon_module -m unittest # mesure uniquement pour 'mon_module'
coverage report                             # affiche le rapport de couverture dans le terminal
coverage report -m                          # affiche les numéros des lignes non couvertes (missing)
coverage html                               # génère un rapport HTML interactif (dossier htmlcov/index.html)

```

```python
# Code de test avec Unittest (test_main.py)
import unittest
from unittest.mock import Mock, patch

class TestMonCode(unittest.TestCase):
    def setUp(self):
        # Exécuté AVANT chaque méthode de test
        self.valeur = 10

    def tearDown(self):
        # Exécuté APRÈS chaque méthode de test
        pass

    def test_cas_simple(self):
        self.assertEqual(1 + 1, 2)
        self.assertTrue(self.valeur > 0)

    def test_exception(self):
        with self.assertRaises(ValueError):
            int("invalide")

    def test_avec_mock(self):
        mock = Mock()
        mock.calculer.return_value = 42
        self.assertEqual(mock.calculer(), 42)

if __name__ == "__main__":
    unittest.main()

```
## Logs & Stack Traces

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

try:
    resultat = 10 / 0
except ZeroDivisionError:
    # (Recommandée) : Inclus automatiquement la stack trace en niveau ERROR
    logger.exception("Échec du calcul")
    # Sur un autre niveau (ex: CRITICAL ou WARNING)
    logger.critical("Erreur critique !", exc_info=True)
```


# Solutions des exercices Python

---

**Chapitre 1 / Exercice 1**

Voici l'instruction en Python pour afficher la version exacte de l'interpréteur :

```python
import sys

print(sys.version)

```

Le module standard `os` permet d'accéder aux variables d'environnement via le dictionnaire `os.environ`.

```python
import os

#Récupération sécurisée de la variable PATH
path_env = os.environ.get("PATH", "Variable non trouvée")
print(path_env)

```

Le module standard `subprocess` est l'outil officiel et sécurisé pour exécuter des commandes système.

```python
import subprocess

#Exécution de la commande shell 'dir' (sur Windows) ou 'ls' (sur Linux/macOS)
résultat = subprocess.run("dir", shell=True, text=True, capture_output=True)

# Affichage de la sortie standard
print(résultat.stdout)

```

> 💡 **Bonne pratique :** Privilégiez `subprocess.run()` avec `shell=True` si vous devez récupérer le texte généré par la commande ou gérer d'éventuelles erreurs.

**Chapitre 1 / Exercice 2**

```python
# La fonction range(1, 11) produit les entiers de 1 à 10
for i in range(1, 11):
    print("O" * i)
```

**Chapitre 2 / Exercice 1**
```python
from pathlib import Path

def saluer(nom: str) -> str:
    """Génère un message de salutation à partir d'un nom."""
    return f"Bonjour {nom}, bienvenue !"

if __name__ == '__main__':
    # Définition du prénom
    prenom = "Karim"
    
    # Génération du message
    message = saluer(prenom)
    
    # Écriture du message dans le fichier bienvenue.txt avec pathlib
    fichier = Path("bienvenue.txt")
    fichier.write_text(message, encoding="utf-8")
    
    # Confirmation dans la console
    print(f"Message écrit dans '{fichier.name}' : {message}")

```

**Chapitre 2 / Exercice 2**
```python
import sys
from pathlib import Path

def est_dans_venv() -> bool:
    """Vérifie si le script est exécuté dans un environnement virtuel (venv)."""
    # sys.prefix != sys.base_prefix indique qu'un environnement virtuel est actif
    return sys.prefix != sys.base_prefix

def verifier_environnement() -> None:
    """Contrôle l'environnement et consigne le statut."""
    log_file = Path("env_status.log")

    if est_dans_venv():
        # Récupération du chemin de l'interpréteur actuel
        executable_path = sys.executable
        log_content = f"Environnement virtuel actif.\nInterpréteur : {executable_path}\n"
        
        # Écriture dans le fichier journal
        log_file.write_text(log_content, encoding="utf-8")
        print(f"[OK] Environnement virtuel détecté. Détails écrits dans {log_file.name}")
    else:
        print("[AVERTISSEMENT] Vous n'êtes pas dans un environnement virtuel !")
        print("Il est fortement recommandé d'en activer un (ex: 'source venv/bin/activate' ou 'venv\\Scripts\\activate').")

if __name__ == "__main__":
    verifier_environnement()
	
```	
**Chapitre 3 / Exercice 1**
```python
def afficher_types() -> None:
    """Déclare quatre variables scalaires et affiche leur type."""
    # Déclaration des quatre variables de types scalaires
    nombre_entier: int = 42
    nombre_decimal: float = 3.14
    est_actif: bool = True
    chaine_texte: str = "Python"

    # Affichage de la valeur et du type de chaque variable
    print(f"Valeur : {nombre_entier:<10} | Type : {type(nombre_entier)}")
    print(f"Valeur : {nombre_decimal:<10} | Type : {type(nombre_decimal)}")
    print(f"Valeur : {str(est_actif):<10} | Type : {type(est_actif)}")
    print(f"Valeur : {chaine_texte:<10} | Type : {type(chaine_texte)}")


if __name__ == "__main__":
    afficher_types()
```	

**Chapitre 3 / Exercice 2**
```python
def calculer_moyenne(notes: list[float]) -> float:
    """Calcule la moyenne d'une liste de notes numériques."""
    if not notes:
        return 0.0

    # Somme des notes divisée par le nombre d'éléments
    total = sum(notes)
    nombre_de_notes = len(notes)
    
    # Stockage dans une variable locale
    moyenne_calculee = total / nombre_de_notes
    
    return moyenne_calculee


if __name__ == "__main__":
    # Liste des notes de l'étudiant
    notes_etudiant = [14.5, 12.0, 16.5, 9.0, 15.0]

    # Appel de la fonction et affichage du résultat
    moyenne_finale = calculer_moyenne(notes_etudiant)
    print(f"Notes de l'étudiant : {notes_etudiant}")
    print(f"Moyenne calculée   : {moyenne_finale:.2f} / 20")```	

**Chapitre 4 / Exercice 1 
```python
def calculer_operations(a: int, b: int) -> None:
    """Calcule et affiche la somme, le produit et le reste de la division entière de deux nombres."""
    somme = a + b
    produit = a * b
    
    # Gestion du cas de la division par zéro
    reste = a % b if b != 0 else None

    print(f"Nombre A : {a}")
    print(f"Nombre B : {b}")
    print(f"Somme (a + b)                : {somme}")
    print(f"Produit (a * b)              : {produit}")
    if reste is not None:
        print(f"Reste de la division (a % b) : {reste}")
    else:
        print("Reste de la division (a % b) : Impossible (division par zéro)")


if __name__ == "__main__":
    # Initialisation des deux variables numériques
    nombre_1 = 25
    nombre_2 = 4

    calculer_operations(nombre_1, nombre_2)
```	
**Chapitre 4 / Exercice 2**
```python
def verifier_acces(age: int, a_autorisation: bool) -> bool:
    """Vérifie si l'utilisateur remplit les conditions d'accès."""
    # Condition : être majeur (>= 18) ET posséder une autorisation
    est_autorise = (age >= 18) and a_autorisation
    return est_autorise


if __name__ == "__main__":
    # Déclaration des variables de test
    age_utilisateur = 20
    a_autorisation = True

    # Vérification des conditions
    acces_accorde = verifier_acces(age_utilisateur, a_autorisation)

    print(f"Âge de l'utilisateur : {age_utilisateur} ans")
    print(f"Possède une autorisation : {a_autorisation}")
    
    if acces_accorde:
        print("Résultat : Accès ACCORDÉ")
    else:
        print("Résultat : Accès REFUSÉ")
```	

**Chapitre 5 / Exercice 1** 
```python
def calculer_prix_ttc(prix_ht_str: str) -> int:
    """Convertit un prix HT sous forme de chaîne, applique la TVA de 20% 
    et renvoie le montant TTC arrondi sous forme d'entier.
    """
    # Conversion de la chaîne en float
    prix_ht = float(prix_ht_str)
    
    # Application de la taxe de 20%
    prix_ttc_float = prix_ht * 1.20
    
    # Conversion du résultat final en int (troncature / arrondi)
    prix_ttc_int = int(prix_ttc_float)
    
    return prix_ttc_int


if __name__ == "__main__":
    # Chaîne initiale représentant le prix avec décimales
    prix_chaine = "49.99"
    
    # Exécution du calcul
    resultat = calculer_prix_ttc(prix_chaine)
    
    print(f"Prix HT initial (str)   : '{prix_chaine}'")
    print(f"Prix TTC converti (int) : {resultat} €")
```	

**Chapitre 5 / Exercice 2**
```python
def observer_conversion_implicite() -> None:
    """Effectue l'addition d'un entier et d'un flottant pour observer le type du résultat."""
    # Déclaration d'un entier (int) et d'un flottant (float)
    nombre_entier: int = 15
    nombre_flottant: float = 4.5

    # Addition des deux variables (conversion implicite par Python)
    resultat = nombre_entier + nombre_flottant

    # Affichage des valeurs et de leurs types
    print(f"Valeur 1 (entier)   : {nombre_entier} | Type : {type(nombre_entier)}")
    print(f"Valeur 2 (flottant) : {nombre_flottant} | Type : {type(nombre_flottant)}")
    print(f"Résultat            : {resultat} | Type : {type(resultat)}")


if __name__ == "__main__":
    observer_conversion_implicite()
```	

**Chapitre 6 / Exercice 1**
```python
def nettoyer_et_capitaliser(texte_brut: str) -> str:
    """Supprime les espaces superflus en début/fin de chaîne 

    et convertit le texte intégralement en majuscules.
    """
    # 1. Suppression des espaces superflus aux extrémités avec strip()
    texte_epure = texte_brut.strip()
    
    # 2. Conversion en majuscules avec upper()
    texte_majuscule = texte_epure.upper()
    
    return texte_majuscule


if __name__ == "__main__":
    # Chaîne initiale avec espaces inutiles et minuscules
    chaine_initiale = "   bienvenue dans le cours de python !   "

    # Application des méthodes de nettoyage
    chaine_nettoyee = nettoyer_et_capitaliser(chaine_initiale)

    print(f"Chaîne initiale : '{chaine_initiale}'")
    print(f"Chaîne nettoyée : '{chaine_nettoyee}'")
```	
**Chapitre 6 / Exercice 2**
```python
def extraire_et_formater(phrase: str, nom_utilisateur: str) -> str:
    """Extrait l'indicatif régional d'un numéro présent dans une phrase

    et génère un message personnalisé à l'aide d'une f-string.
    """
    # Slicing des 2 premiers caractères ([début:fin])
    indicatif = phrase[:2]

    # Formatage du message personnalisé avec une f-string
    message_formate = f"Bonjour {nom_utilisateur}, votre indicatif régional est le +{indicatif}."

    return message_formate


if __name__ == "__main__":
    # Chaîne initiale avec le numéro au début de la phrase
    phrase_telephone = "33 6 12 34 56 78 est le numéro de contact."
    prenom = "Karim"

    # Extraction et génération du message
    resultat = extraire_et_formater(phrase_telephone, prenom)

    print(f"Phrase source : '{phrase_telephone}'")
    print(f"Message généré : {resultat}")
```	

**Chapitre 7 / Exercice 1** 
```python
import random

def analyser_parite_liste(taille: int = 10) -> tuple[int, int]:
    """Génère une liste de nombres aléatoires et compte les éléments pairs et impairs."""
    # Génération d'une liste de 10 valeurs aléatoires entre 0 et 99 inclus
    valeurs: list[int] = [random.randrange(100) for _ in range(taille)]
    
    compteur_pairs: int = 0
    compteur_impairs: int = 0

    # Parcours du tableau
    for nombre in valeurs:
        if nombre % 2 == 0:
            compteur_pairs += 1
        else:
            compteur_impairs += 1

    # Affichage des détails
    print(f"Liste générée : {valeurs}")
    print(f"Nombres pairs   : {compteur_pairs}")
    print(f"Nombres impairs : {compteur_impairs}")

    return compteur_pairs, compteur_impairs


if __name__ == "__main__":
    analyser_parite_liste()
```	

**Chapitre 7 / Exercice 2**
```python
def assembler_noms_et_ages(noms: list[str], ages: list[int]) -> dict[str, int]:
    """Assemble deux listes (noms et âges) pour former un dictionnaire nom: âge."""
    # Dictionnaire résultat
    annuaire: dict[str, int] = {}

    # Option 1 : Assemblage avec une boucle basée sur les indices
    for i in range(len(noms)):
        cle = noms[i]
        valeur = ages[i]
        annuaire[cle] = valeur

    return annuaire


if __name__ == "__main__":
    # Déclaration des deux listes
    liste_noms = ["toto1", "toto2", "toto3", "toto4"]
    liste_ages = [20, 25, 30, 35]

    # Appel de la fonction
    resultat = assembler_noms_et_ages(liste_noms, liste_ages)

    print(f"Liste des noms : {liste_noms}")
    print(f"Liste des âges : {liste_ages}")
    print(f"Dictionnaire  : {resultat}")
```	

**Chapitre 7 / Exercice 3**
```python
import random

def separer_parite(taille: int = 10) -> tuple[list[int], list[int]]:
    """Génère une liste d'entiers aléatoires et la sépare en deux listes : 

    l'une contenant les nombres pairs, l'autre les nombres impairs.
    """
    # Génération d'un tableau de 10 valeurs aléatoires entre 0 et 99
    valeurs: list[int] = [random.randrange(100) for _ in range(taille)]
    
    # Initialisation des deux listes réceptrices
    pairs: list[int] = []
    impairs: list[int] = []

    # Parcours du tableau initial
    for nombre in valeurs:
        if nombre % 2 == 0:
            pairs.append(nombre)
        else:
            impairs.append(nombre)

    # Affichage des résultats
    print(f"Tableau initial : {valeurs}")
    print(f"Tableau pairs   : {pairs}")
    print(f"Tableau impairs : {impairs}")

    return pairs, impairs


if __name__ == "__main__":
    separer_parite()
```	

**Chapitre 8 / Exercice 1** 
```python
def traiter_liste_imbriquee(nombre_elements: int = 5) -> list[list[object]]:
    """Génère une liste de sous-listes [nom, entier] 

    puis parcourt la structure pour afficher uniquement les noms.
    """
    liste_principale: list[list[object]] = []

    # 1. Génération de la liste de sous-listes via une boucle
    for i in range(1, nombre_elements + 1):
        nom = f"TOTO{i}"
        sous_liste = [nom, i]
        liste_principale.append(sous_liste)

    print(f"Liste générée : {liste_principale}\n")
    print("Affichage des noms uniquement :")

    # 2. Parcours de la liste imbriquée et extraction du premier élément
    for sous_liste in liste_principale:
        nom = sous_liste[0]  # Récupération de l'élément à l'index 0 ('TOTOx')
        print(nom)

    return liste_principale


if __name__ == "__main__":
    traiter_liste_imbriquee()
```	
**Chapitre 8 / Exercice 2**
```python
def traiter_liste_dictionnaires(nombre_elements: int = 5) -> list[dict[str, object]]:
    """Génère une liste de dictionnaires {'nom': str, 'age': int}

    puis parcourt la structure pour afficher uniquement les noms.
    """
    liste_personnes: list[dict[str, object]] = []

    # 1. Génération de la liste de dictionnaires via une boucle
    for i in range(1, nombre_elements + 1):
        personne = {
            "nom": f"TOTO{i}",
            "age": i
        }
        liste_personnes.append(personne)

    print(f"Liste générée : {liste_personnes}\n")
    print("Affichage des noms uniquement :")

    # 2. Parcours de la liste et extraction de la valeur associée à la clé 'nom'
    for personne in liste_personnes:
        nom = personne["nom"]
        print(nom)

    return liste_personnes


if __name__ == "__main__":
    traiter_liste_dictionnaires()
```	

**Chapitre 8 / Exercice 3**
```python
def filtrer_fruits_par_prix(catalogue: dict[str, float], prix_seuil: float) -> None:
    """Parcourt le dictionnaire de fruits et affiche ceux dont le prix dépasse le seuil fixé."""
    print(f"Catalogue des fruits coûtant strictement plus de {prix_seuil:.2f} € :\n")

    # Parcours simultané des clés (fruits) et des valeurs (prix) via .items()
    for fruit, prix in catalogue.items():
        if prix > prix_seuil:
            print(f"- {fruit.capitalize():<10} : {prix:.2f} €")


if __name__ == "__main__":
    # Dictionnaire associant chaque fruit à son prix unitaire en euros
    prix_fruits: dict[str, float] = {
        "pomme": 1.50,
        "ananas": 3.80,
        "banane": 0.90,
        "mangue": 2.50,
        "orange": 1.20,
        "fraise": 4.20
    }

    seuil_defaut = 2.00
    filtrer_fruits_par_prix(prix_fruits, seuil_defaut)
```	

**Chapitre 9 / Exercice 1** 
```python
def calculer_moyenne_args(*nombres: int) -> float:
    """Calcule la moyenne arithmétique d'un nombre indéfini d'entiers."""
    # *nombres est un tuple contenant tous les arguments transmis
    if not nombres:
        return 0.0

    total = sum(nombres)
    quantite = len(nombres)

    return total / quantite


if __name__ == "__main__":
    # Exemples d'appels avec un nombre variable d'arguments
    moyenne_1 = calculer_moyenne_args(10, 12, 14, 16)
    moyenne_2 = calculer_moyenne_args(5, 15, 20)
    moyenne_vide = calculer_moyenne_args()

    print(f"Moyenne (10, 12, 14, 16) : {moyenne_1:.2f}")
    print(f"Moyenne (5, 15, 20)      : {moyenne_2:.2f}")
    print(f"Moyenne (aucun argument) : {moyenne_vide:.2f}")
```	

**Chapitre 9 / Exercice 2**
```python
from typing import Callable

def appliquer_operation(
    fonction_math: Callable[[float, float], float], 
    a: float, 
    b: float
) -> float:
    """Applique la fonction mathématique passée en paramètre aux deux nombres a et b."""
    return fonction_math(a, b)


# Exemples de fonctions à passer en paramètre
def additionner(x: float, y: float) -> float:
    return x + y

def multiplier(x: float, y: float) -> float:
    return x * y


if __name__ == "__main__":
    nombre_1 = 12.0
    nombre_2 = 4.0

    # Passage de fonctions nommées en argument
    res_addition = appliquer_operation(additionner, nombre_1, nombre_2)
    res_multiplication = appliquer_operation(multiplier, nombre_1, nombre_2)

    # Passage d'une fonction anonyme (lambda)
    res_puissance = appliquer_operation(lambda x, y: x ** y, nombre_1, nombre_2)

    print(f"Addition ({nombre_1} + {nombre_2})        : {res_addition}")
    print(f"Multiplication ({nombre_1} * {nombre_2})  : {res_multiplication}")
    print(f"Puissance ({nombre_1} ^ {nombre_2})       : {res_puissance}")
```	

**Chapitre 10 / Exercice 1** 
```python
def filtrer_mots_longs(mots: list[str], longueur_min: int = 5) -> list[str]:
    """Extrait d'une liste les mots ayant une longueur strictement supérieure à longueur_min."""
    # Utilisation de filter() avec une expression lambda
    iterateur_mots_longs = filter(lambda mot: len(mot) > longueur_min, mots)
    
    # Conversion de l'itérateur filter en liste
    return list(iterateur_mots_longs)


if __name__ == "__main__":
    # Liste initiale de mots
    liste_mots = ["arbre", "soleil", "ordinateur", "clef", "python", "code", "développement"]

    # Exécution du filtrage
    mots_filtres = filtrer_mots_longs(liste_mots, 5)

    print(f"Liste d'origine : {liste_mots}")
    print(f"Mots de plus de 5 caractères : {mots_filtres}")
```	
**Chapitre 10 / Exercice 2**
```python
from functools import reduce

def calculer_produit_liste(nombres: list[int]) -> int:
    """Calcule le produit cumulé de tous les entiers d'une liste via reduce()."""
    if not nombres:
        return 0

    # reduce() applique la fonction lambda cumulée sur la liste
    produit_total = reduce(lambda acc, val: acc * val, nombres)
    
    return produit_total


if __name__ == "__main__":
    # Liste initiale d'entiers
    liste_nombres = [2, 3, 4, 5]

    # Calcul du produit
    resultat = calculer_produit_liste(liste_nombres)

    print(f"Liste d'entiers : {liste_nombres}")
    print(f"Produit total    : {resultat}")
```	

**Chapitre 11 / Exercice 1** 
```python
from typing import Generator

def generer_nombres_pairs(limite: int) -> Generator[int, None, None]:
    """Générateur produisant les nombres pairs de 0 jusqu'à la limite incluse."""
    actuel = 0
    while actuel <= limite:
        yield actuel
        actuel += 2


if __name__ == "__main__":
    limite_maximale = 10

    print(f"Séquence des nombres pairs jusqu'à {limite_maximale} :")
    
    # Parcours du générateur à l'aide d'une boucle for
    for nombre in generer_nombres_pairs(limite_maximale):
        print(nombre, end=" ")
    print()  # Saut de ligne final
```	
**Chapitre 11 / Exercice 2**
```python
from typing import Iterator

def consommer_expression_generatrice() -> None:
    """Instancie une expression génératrice pour les carrés de 1 à 10

    et extrait chaque valeur séquentiellement avec next().
    """
    # Expression génératrice entourée de parenthèses (évaluation paresseuse)
    carres_gen: Iterator[int] = (x ** 2 for x in range(1, 11))

    print("Extraction manuelle des valeurs avec next() :\n")

    # Récupération de la première valeur
    premier = next(carres_gen)
    print(f"Premier élément  : {premier}")

    # Récupération de la deuxième valeur
    deuxieme = next(carres_gen)
    print(f"Deuxième élément : {deuxieme}")

    # Récupération de la troisième valeur
    troisieme = next(carres_gen)
    print(f"Troisième élément: {troisieme}")

    # Parcoure le reste des valeurs générées
    print("\nParcours du reste du générateur :")
    for valeur in carres_gen:
        print(valeur, end=" ")
    print()


if __name__ == "__main__":
    consommer_expression_generatrice()
```	

**Chapitre 12 / Exercice 1** 
```python
def demander_nombre_entier() -> int:
    """Demande un nombre entier à l'utilisateur et gère l'exception ValueError

    en cas de saisie invalide.
    """
    saisie = input("Veuillez saisir un nombre entier : ")

    try:
        # Tentative de conversion de la chaîne en entier
        nombre = int(saisie)
        print(f"Conversion réussie : vous avez saisi le nombre {nombre}.")
        return nombre

    except ValueError:
        # Interception de l'erreur si la saisie n'est pas un nombre valide
        print(f"Erreur de saisie : '{saisie}' n'est pas un nombre entier valide.")
        return 0


if __name__ == "__main__":
    demander_nombre_entier()
```	

**Chapitre 12 / Exercice 2**
```python
def valider_mot_de_passe(mot_de_passe: str) -> bool:
    """Vérifie la longueur minimale d'un mot de passe.

    Lève une exception ValueError si la longueur est inférieure à 8 caractères.
    """
    longueur_minimale = 8

    # Vérification de la contrainte de longueur
    if len(mot_de_passe) < longueur_minimale:
        raise ValueError(
            f"Mot de passe trop court ({len(mot_de_passe)} caractères). "
            f"Il doit contenir au moins {longueur_minimale} caractères."
        )

    print("Mot de passe valide.")
    return True


if __name__ == "__main__":
    # Test avec un mot de passe trop court
    mots_de_passe_test = ["pass123", "Securite2026!"]

    for mdp in mots_de_passe_test:
        print(f"\nTest du mot de passe : '{mdp}'")
        try:
            valider_mot_de_passe(mdp)
        except ValueError as erreur:
            print(f"Exception capturée : {erreur}")
```	

**Chapitre 13 / Exercice 1** 
```python
def afficher_bienvenue(nom_utilisateur: str) -> None:
    """Affiche un message de bienvenue personnalisé."""
    print(f"Bienvenue, {nom_utilisateur} ! Le script s'exécute correctement.")


if __name__ == "__main__":
    # Ce bloc ne s'exécute que si le fichier est lancé directement
    print("Exécution du script en tant que programme principal.")
    
    nom = "Karim"
    afficher_bienvenue(nom)
```	
**Chapitre 13 / Exercice 2**
```python
import sys

def saluer_utilisateur() -> None:
    """Récupère le nom passé en argument de ligne de commande via sys.argv

    et affiche une salutation personnalisée.
    """
    # sys.argv[0] contient toujours le nom du script lui-même.
    # On vérifie si un argument supplémentaire a été transmis.
    if len(sys.argv) < 2:
        print("Erreur : Aucun nom n'a été fourni en argument.")
        print(f"Usage : python {sys.argv[0]} <votre_nom>")
        sys.exit(1)

    # Extraction du premier argument après le nom du script
    nom_utilisateur: str = sys.argv[1]
    print(f"Bonjour {nom_utilisateur}, ravi de vous rencontrer !")


if __name__ == "__main__":
    saluer_utilisateur()
```	

**Chapitre 14 / Exercice 1** 
```python
from pathlib import Path

def exporter_notes() -> None:
    """Crée un dossier 'export', y écris un fichier 'notes.txt' avec 3 lignes

    et affiche la taille du fichier en octets.
    """
    # Définition des chemins avec pathlib
    dossier_export = Path("export")
    fichier_notes = dossier_export / "notes.txt"

    # 1. Création du dossier 'export' s'il n'existe pas
    dossier_export.mkdir(parents=True, exist_ok=True)

    # Contenu de 3 lignes à écrire dans le fichier
    lignes = [
        "Première ligne : Introduction à la gestion des fichiers en Python.\n",
        "Deuxième ligne : Utilisation orientée objet de pathlib.Path.\n",
        "Troisième ligne : Export et calcul de métadonnées terminé.\n"
    ]

    # 2. Écriture du fichier texte avec encodage UTF-8
    with open(fichier_notes, mode="w", encoding="utf-8") as fichier:
        fichier.writelines(lignes)

    print(f"Fichier créé avec succès : {fichier_notes.resolve()}")

    # 3. Récupération et affichage de la taille du fichier
    taille_octets = fichier_notes.stat().st_size
    print(f"Taille du fichier : {taille_octets} octets")


if __name__ == "__main__":
    exporter_notes()
```	
**Chapitre 14 / Exercice 2**
```python
import zipfile
from pathlib import Path

def archiver_fichiers_python(dossier_source: str | Path, nom_archive: str = "modules.zip") -> Path | None:
    """Recherche tous les fichiers .py dans le dossier_source (sans sous-dossiers)

    et les regroupe dans une archive ZIP nommée nom_archive.
    """
    chemin_dossier = Path(dossier_source)
    chemin_archive = chemin_dossier / nom_archive

    # Vérification de l'existence du dossier source
    if not chemin_dossier.is_dir():
        print(f"Erreur : Le dossier '{chemin_dossier}' n'existe pas ou n'est pas un répertoire.")
        return None

    # Recherche de tous les fichiers .py présents à la racine du dossier
    fichiers_py = list(chemin_dossier.glob("*.py"))

    if not fichiers_py:
        print(f"Aucun fichier .py trouvé dans {chemin_dossier}.")
        return None

    print(f"Fichiers Python trouvés ({len(fichiers_py)}) :")
    for f in fichiers_py:
        print(f" - {f.name}")

    # Création et écriture dans l'archive ZIP
    with zipfile.ZipFile(chemin_archive, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for fichier in fichiers_py:
            # arcname garantit d'inclure uniquement le nom du fichier dans l'archive (sans l'arborescence complète)
            archive.write(fichier, arcname=fichier.name)

    print(f"\nArchive créée avec succès : {chemin_archive.resolve()}")
    print(f"Taille de l'archive : {chemin_archive.stat().st_size} octets")

    return chemin_archive


if __name__ == "__main__":
    # Test d'archivage sur le répertoire courant '.'
    archiver_fichiers_python(dossier_source=".")
```	

**Chapitre 15 / Exercice 1** 
```bash
python -m venv env_projet
source env_projet/bin/activate
deactivate
```	
**Chapitre 15 / Exercice 2**
```bash
# Activation de l'environnement
source env_projet/bin/activate

# Vérification de l'exécutable Python actif
which python

# Désactivation de l'environnement
deactivate
```	
**Chapitre 16 / Exercice 1** 
```python
from pathlib import Path

def creer_fichier_unicode(nom_fichier: str = "notes.txt") -> None:
    """Crée un fichier texte spécifié avec l'encodage UTF-8

    et y inscrit une phrase contenant des caractères accentués.
    """
    chemin_fichier = Path(nom_fichier)

    # Texte à inscrire contenant divers caractères accentués et spéciaux
    contenu: str = (
        "Apprendre à programmer en Python est une activité très enrichissante !\n"
        "Gérer correctement l'encodage UTF-8 garantit une lisibilité universelle."
    )

    # Ouverture du fichier en mode écriture ("w") avec encodage explicite utf-8
    with open(chemin_fichier, mode="w", encoding="utf-8") as fichier:
        fichier.write(contenu)

    print(f"Le fichier '{chemin_fichier.name}' a été créé avec succès en encodage UTF-8.")


if __name__ == "__main__":
    creer_fichier_unicode()
```	
**Chapitre 16 / Exercice 2**
```python
from pathlib import Path

def lire_fichier_unicode(nom_fichier: str = "notes.txt") -> None:
    """Ouvre et lit le contenu global d'un fichier texte au format UTF-8,

    puis l'affiche dans la console.
    """
    chemin_fichier = Path(nom_fichier)

    # Vérification préalable de l'existence du fichier
    if not chemin_fichier.is_file():
        print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
        return

    # Ouverture du fichier en mode lecture ("r") avec encodage UTF-8
    with open(chemin_fichier, mode="r", encoding="utf-8") as fichier:
        contenu: str = fichier.read()

    print(f"--- Contenu de '{chemin_fichier.name}' ---")
    print(contenu)


if __name__ == "__main__":
    lire_fichier_unicode()
```	

**Chapitre 17 / Exercice 1** 
```python
class Livre:
    """Représente un livre avec un titre et un auteur."""

    def __init__(self, titre: str, auteur: str) -> None:
        """Initialise les attributs de l'instance Livre."""
        self.titre: str = titre
        self.auteur: str = auteur

    def obtenir_description(self) -> str:
        """Retourne une description textuelle complète de l'ouvrage."""
        return f"« {self.titre} » par {self.auteur}"


if __name__ == "__main__":
    # Instanciation de deux objets Livre
    livre_1 = Livre("Le Comte de Monte-Cristo", "Alexandre Dumas")
    livre_2 = Livre("L'Étranger", "Albert Camus")

    # Appel de la méthode de description
    print(livre_1.obtenir_description())
    print(livre_2.obtenir_description())
```	
**Chapitre 17 / Exercice 2**
```python
class Livre:
    """Représente un livre avec un titre et un auteur."""

    def __init__(self, titre: str, auteur: str) -> None:
        self.titre: str = titre
        self.auteur: str = auteur

    def obtenir_description(self) -> str:
        """Retourne une description textuelle de l'ouvrage."""
        return f"« {self.titre} » par {self.auteur}"


class LivreNumerique(Livre):
    """Représente un livre numérique, héritant de Livre,

    avec une propriété supplémentaire pour la taille du fichier.
    """

    def __init__(self, titre: str, auteur: str, taille_mo: float) -> None:
        # Appel du constructeur de la classe parente (Livre)
        super().__init__(titre, auteur)
        # Attribut propre à la classe fille
        self.taille_mo: float = taille_mo

    def obtenir_description(self) -> str:
        """Surcharge de la méthode parente pour inclure la taille du fichier."""
        description_base = super().obtenir_description()
        return f"{description_base} [Ebook - {self.taille_mo} Mo]"


if __name__ == "__main__":
    # Instanciation d'un objet LivreNumerique
    ebook = LivreNumerique("Apprendre Python", "Karim Belhadj", 4.5)

    # Affichage de la description
    print(ebook.obtenir_description())
    print(f"Taille du fichier : {ebook.taille_mo} Mo")
```	
**Chapitre 18 / Exercice 1** 
```python
import asyncio

async def t1():
    print("Début du traitement t1 (1s)...")
    await asyncio.sleep(1)
    print("Fin de t1")
    return "fin de traitement"

async def t2():
    print("Début du traitement t2 (3s)...")
    await asyncio.sleep(3)
    print("Fin de t2")
    return "fin de traitement"

async def main():
    # Exécution simultanée des deux coroutines
    resultats = await asyncio.gather(t1(), t2())
    print("Valeurs de retour :", resultats)

if __name__ == '__main__':
    asyncio.run(main())

```

**Commande d'exécution :**

```bash
python exo1_async.py

```
**Chapitre 18 / Exercice 2** 
```python
import asyncio

async def t1():
    print("Début du traitement t1 (1s)...")
    await asyncio.sleep(1)
    print("Fin de t1")
    return "fin de traitement"

async def t2():
    print("Début du traitement t2 (3s)...")
    await asyncio.sleep(3)
    print("Fin de t2")
    return "fin de traitement"

async def main():
    # Lancement de t1 normalement
    res_t1 = await t1()
    print("Résultat t1 :", res_t1)

    # Lancement de t2 (3s) sous la limite d'un timeout de 2.0s
    try:
        res_t2 = await asyncio.wait_for(t2(), timeout=2.0)
        print("Résultat t2 :", res_t2)
    except asyncio.TimeoutError:
        print("Erreur : Le délai de traitement pour t2 a été dépassé (TimeoutError).")

if __name__ == '__main__':
    asyncio.run(main())

```

```bash
python exo2_async.py

```
**Chapitre 19 / Exercice 1** 
```python
import sqlite3
from pathlib import Path

def initialiser_base_de_donnees(nom_bdd: str = "inventaire.db") -> None:
    """Crée une base de données SQLite, génère la table 'produits'

    et y insère un enregistrement de test avec commit.
    """
    chemin_bdd = Path(nom_bdd)

    # Connexion à la base de données (le fichier est créé s'il n'existe pas)
    with sqlite3.connect(chemin_bdd) as connexion:
        cursor = connexion.cursor()

        # 1. Création de la table produits
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prix REAL NOT NULL
            )
        """)

        # 2. Insertion d'un enregistrement à l'aide de requêtes préparées (?)
        produit_test = ("Clavier mécanique", 89.99)
        cursor.execute("""
            INSERT INTO produits (nom, prix)
            VALUES (?, ?)
        """, produit_test)

        # 3. Validation explicite des modifications
        connexion.commit()

        print(f"Base de données '{chemin_bdd.name}' initialisée avec succès.")
        print(f"Produit ajouté : {produit_test[0]} à {produit_test[1]} €")


if __name__ == "__main__":
    initialiser_base_de_donnees()
```	

**Chapitre 19 / Exercice 2**
```python
import sqlite3
from pathlib import Path

def rechercher_produits_par_prix_max(prix_max: float, nom_bdd: str = "inventaire.db") -> None:
    """Récupère et affiche les produits dont le prix est strictement inférieur

    au seuil passé en paramètre.
    """
    chemin_bdd = Path(nom_bdd)

    if not chemin_bdd.is_file():
        print(f"Erreur : La base de données '{chemin_bdd}' est introuvable.")
        return

    # Connexion à la base de données
    with sqlite3.connect(chemin_bdd) as connexion:
        cursor = connexion.cursor()

        # Requête SELECT avec clause WHERE et paramètre sécurisé (?)
        requete = "SELECT id, nom, prix FROM produits WHERE prix < ?"
        cursor.execute(requete, (prix_max,))

        # Récupération de l'ensemble des résultats
        produits = cursor.fetchall()

        print(f"--- Produits dont le prix est inférieur à {prix_max:.2f} € ---")
        
        if not produits:
            print("Aucun produit ne correspond à ce critère.")
            return

        for produit_id, nom, prix in produits:
            print(f"ID: {produit_id} | Nom: {nom:<20} | Prix: {prix:.2f} €")


if __name__ == "__main__":
    # Recherche des produits dont le prix est inférieur à 100.00 €
    rechercher_produits_par_prix_max(100.0)
```	

**Chapitre 20 / Exercice 1**

Code source (`statistiques.py`)

```python
import random

def aleatoire(minimum=0, maximum=20):
    return random.randint(minimum, maximum)

```

Test unitaire (`test_exercice1.py`)

```python
import unittest
import random
from statistiques import aleatoire

class TestFonctionAleatoire(unittest.TestCase):

    def test_parite_tirages(self):
        # Utilisation d'une graine pour garantir la répétabilité du test aléatoire
        random.seed(42)
        tirages = [aleatoire(0, 20) for _ in range(100)]
        
        paires = sum(1 for val in tirages if val % 2 == 0)
        impaires = sum(1 for val in tirages if val % 2 != 0)
        
        self.assertEqual(paires, impaires)

if __name__ == '__main__':
    unittest.main()

```

**Chapitre 20 / Exercice 2**

Code source (`outils.py`)

```python
import random

class Aleatoire:
    def __init__(self, minimum=0, maximum=20):
        self.minimum = minimum
        self.maximum = maximum

    def generer(self):
        return random.randint(self.minimum, self.maximum)

```

Test unitaire (`test_exercice2.py`)

```python
import unittest
import random
from outils import Aleatoire

class TestClasseAleatoire(unittest.TestCase):

    def setUp(self):
        self.generateur = Aleatoire(0, 20)

    def test_parite_tirages_classe(self):
        random.seed(42)
        tirages = [self.generateur.generer() for _ in range(100)]
        
        paires = sum(1 for val in tirages if val % 2 == 0)
        impaires = sum(1 for val in tirages if val % 2 != 0)
        
        self.assertEqual(paires, impaires)

if __name__ == '__main__':
    unittest.main()

```
Commandes pour la couverture (`coverage`)

```bash
# Exécution du test avec mesure
coverage run -m unittest test_exercice2.py

# Rapport console pour le fichier outils.py
coverage report -m outils.py

# Rapport HTML
coverage html

```