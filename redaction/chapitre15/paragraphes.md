# Chapitre 15 : Environnement virtuel adapté à chaque application

La création d'environnements virtuels permet d'isoler les dépendances de chaque application Python pour éviter les conflits entre les bibliothèques installées sur le système. Maîtriser ces outils est indispensable pour garantir la stabilité et la reproductibilité de vos projets.
Dans ce chapitre :

* Création d'un contexte Python isolé avec `venv`

* Utilisation des scripts d'activation et de désactivation (`activate`/`deactivate`)



---

## Création d'un context python isolé avec venv

Le module `venv` permet de générer un répertoire de travail contenant une copie autonome de l'interpréteur Python et de sa bibliothèque standard. Cela isole complètement l'environnement des paquets globaux de la machine.

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

## Exemple de synthèse

```bash
# Séquence complète de commandes pour configurer et utiliser un environnement virtuel sous Linux/macOS :

# 1. Création du contexte Python isolé
python -m venv mon_env

# 2. Activation de l'environnement virtuel
source mon_env/bin/activate

# 3. Installation d'une bibliothèque tierce dans cet environnement isolé
pip install requests

# 4. Sortie de l'environnement virtuel
deactivate

```

## Exercices

1. **Exercice 1 :** Exécutez la commande dans votre terminal pour créer un environnement virtuel nommé `env_projet` à la racine de votre dossier de travail.
2. **Exercice 2 :** Activez l'environnement virtuel créé, vérifiez son bon fonctionnement, puis désactivez-le à l'aide de la commande appropriée.
