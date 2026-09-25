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
    # 1. Création du parseur avec une description pour l'aide
    parser = argparse.ArgumentParser(
        description="Script de sauvegarde de dossier."
    )

    # 2. Définition de l'argument obligatoire (positionnel)
    parser.add_argument(
        "folder",
        type=str,
        help="Chemin du dossier à sauvegarder",
    )

    # 3. Analyse des arguments de la ligne de commande
    args = parser.parse_args()

    # 4. Appel de la fonction avec l'argument récupéré
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
  

## Gestion de package - pip

L'outil `pip` est le gestionnaire de paquets officiel de Python qui permet d'installer, de mettre à jour et de supprimer des bibliothèques tierces depuis le Python Package Index (PyPI).

```bash
# Installation d'un package tiers en ligne de commande (exemple)
pip install requests

```

> 💡 Utilisez systématiquement un environnement virtuel (`venv`) avant d'installer des packages avec `pip` pour isoler les dépendances de vos différents projets.

---

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
