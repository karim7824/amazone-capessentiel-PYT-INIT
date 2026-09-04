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

> 💡 **Bonne pratique :** Vérifiez toujours après l'installation que la commande `python --version` (ou `python3 --version`) répond correctement dans votre invite de commande.

## Créer un projet Python main.py avec la condition `__name__ == '__main__'`

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

### Exemple de synthèse

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

### Exercices de fin de chapitre

1.  **Exercice 1 : Création et exécution d'un script structuré**
Créez un fichier nommé `main.py` qui définit une fonction `saluer(nom)`. Dans le bloc principal `if __name__ == '__main__':`, appelez cette fonction avec votre prénom, puis faites en sorte que le programme écrive le message de salutation dans un fichier texte nommé `bienvenue.txt`.
2.  **Exercice 2 : Générateur d'environnement et vérification venv**
Écrivez un script Python nommé `check_env.py` qui teste si le programme est exécuté au sein d'un environnement virtuel `venv`. Si ce n'est pas le cas, le script doit afficher un avertissement recommandant d'activer un environnement virtuel. Si l'environnement virtuel est actif, le script doit inscrire le chemin de l'interpréteur dans un fichier `env_status.log`.
