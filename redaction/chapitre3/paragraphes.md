# Chapitre 3 : Définir et manipuler des données types en mémoire

Maîtriser les types de données et leur manipulation en mémoire est essentiel pour stocker et traiter efficacement l'information. Ces concepts fondamentaux garantissent la rigueur et la logique de vos programmes en Python.
Dans ce chapitre :

* Déclaration et affectation de variables
* Types scalaires (int, float, bool, str)
* Types agrégés (list, tuple, dict, set)
* Valeurs littérales et portée des variables (locale, globale)

---

## Déclaration de variables

En Python, la déclaration d'une variable se fait simplement par affectation d'une valeur à un nom, sans nécessiter de typage explicite préalable. Le type est déduit dynamiquement par l'interpréteur lors de l'exécution.

```python
# Déclaration et initialisation de variables de types différents
age = 42          # Un entier (int)
nom = "Alice"     # Une chaîne de caractères (str)

```

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

### 4. Littéraux de Collections (Structures de données)

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

impedance = 3 + 4j         # Littéral complexe (partie imaginaire avec 'j' ou 'J')
> 💡 Évitez les "nombres magiques" en remplaçant les valeurs littérales numériques répétées par des constantes explicites en début de script.

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

### Exemple de synthèse

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

### Exercices de fin de chapitre

1. **Exercice 1 : variables scalaires** Écrivez un script qui déclare quatre variables de types scalaires différents (`int`, `float`, `bool`, `str`), puis affichez le type de chacune d'elles à l'aide de la fonction `type()`.
2. **Exercice 2 : liste** Créez une liste contenant les notes d'un étudiant, écrivez une fonction qui calcule la moyenne de ces notes, et stockez le résultat dans une variable locale avant de le retourner.
