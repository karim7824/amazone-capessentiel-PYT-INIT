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

### Slicing appliqué aux listes

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

### Parcourir avec l'index et la valeur (`enumerate`)

```python
utilisateurs = ["Alice", "Bob", "Charlie"]

# Permet de récupérer l'index et la valeur à chaque itération
for index, nom in enumerate(utilisateurs, start=1):
    print(f"Utilisateur n°{index} : {nom}")

```

### Parcourir et filtrer avec une compréhension de liste

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

### Parcours et extraction (items, keys, values)

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

### Parcourir les clés et les valeurs simultanément (`items()`)

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

### 1. Fonctions et méthodes essentielles sur les ensembles

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

### 2. Opérations mathématiques sur les ensembles

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

### 1. Parcourir directement les éléments (`for ... in`)

Comme un `set` est une collection non ordonnée, le parcours se fait élément par élément :

```python
langages = {"Python", "Java", "TypeScript", "C++"}

for langage in langages:
    print(f"Langage disponible : {langage}")

```
---

### Parcourir et filtrer avec une compréhension d'ensemble (*Set Comprehension*)

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
