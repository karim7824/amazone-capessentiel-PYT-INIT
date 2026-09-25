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

```

> 💡 **Bonne pratique :** Utilisez toujours le mot-clé `with` pour la manipulation de fichiers afin de garantir leur fermeture automatique même en cas d'erreur.

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
