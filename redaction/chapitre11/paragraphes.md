# Chapitre 11 : Script python en ligne de commande et passage d'arguments

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

Le passage d'arguments en ligne de commande permet de transmettre des paramètres dynamiques à un script lors de son lancement depuis le terminal, notamment via le module standard `sys` ou `argparse`.

```python
import sys

# Récupération des arguments passés en ligne de commande
arguments = sys.argv
nom_script = sys.argv[0]

```

> 💡 Privilégiez l'utilisation du module `argparse` pour les scripts complexes afin de gérer automatiquement l'aide, les options obligatoires et les types d'arguments.

---

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

## Exercices

1. **Exercice 1 :** Écrivez un script Python comportant une structure `if __name__ == "__main__":` qui affiche un message de bienvenue personnalisé lorsque le fichier est exécuté directement.
2. **Exercice 2 :** Utilisez le module `sys` pour récupérer un nom passé en argument dans le terminal et affichez une salutation personnalisée intégrant ce paramètre.