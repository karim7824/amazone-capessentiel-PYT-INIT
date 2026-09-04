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

Voici les **12 méthodes de chaînes de caractères (string) indispensables** en Python, regroupées par usage avec un exemple minimaliste :

---

### 1. Nettoyage et casse

```python
s = "  Python  "

# 1. strip() : Supprime les espaces (ou caractères) au début et à la fin
s.strip()               # "Python"

# 2. lower() : Passe tout le texte en minuscules
"PyThOn".lower()        # "python"

# 3. upper() : Passe tout le texte en majuscules
"python".upper()        # "PYTHON"

# 4. capitalize() : Met la première lettre en majuscule
"python".capitalize()   # "Python"

```

---

### 2. SÉPARATION ET JONCTION

```python
# 5. split() : Découpe une chaîne en liste selon un séparateur (espace par défaut)
"a,b,c".split(",")      # ['a', 'b', 'c']

# 6. join() : Assemble les éléments d'une liste en une seule chaîne
"-".join(['a', 'b'])    # "a-b"

```

---

### 3. RECHERCHE ET REMPLACEMENT

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

### 4. VÉRIFICATION DE CONTENU (RETOURNENT UN BOULÉEN)

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

### Exemple de code

```python
nom = "Alice"
age = 30
prix = 19.99

# 1. Formatage avec l'opérateur % (ancien style - style C)
# %s = string, %d = integer, %.2f = float avec 2 décimales
message_percent = "Bonjour %s, vous avez %d ans. Total : %.2f €" % (nom, age, prix)
print(message_percent)

# 2. Formatage avec la méthode .format() (style Python 2.6+)
# Les accolades {} servent de réceptacles
message_format = "Bonjour {}, vous avez {} ans. Total : {:.2f} €".format(nom, age, prix)
print(message_format)

# Variante avec clés nommées (très pratique pour la lisibilité)
message_nomme = "Bonjour {n}, vous avez {a} ans.".format(n=nom, a=age)
print(message_nomme)

```

---

### Résumé des spécificateurs courants

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

### Formule générale

La syntaxe utilise des crochets séparés par deux-points (`:`), et non des virgules :

$$\mathbf{[début : fin : pas]}$$

---

### Signification des paramètres

* **`début`** *(n)* : L'index du premier élément inclus. S'il est omis, la sélection commence au début (`0`).
* **`fin`** *(m)* : L'index du premier élément **exclu** (la sélection s'arrête juste avant cet index). S'il est omis, la sélection va jusqu'à la fin de la séquence.
* **`pas`** : Le saut entre chaque élément retenu (positif pour aller vers l'avant, négatif pour aller en arrière). Par défaut, il vaut `1`.

---

### Exemples d'application

```python
texte = "Python"
# Index :  0   1   2   3   4   5
#         'P' 'y' 't' 'h' 'o' 'n'

# 1. Extraction standard : du caractère index 0 à l'index 4 exclu
print(texte[0:4])       # "Pyth"

# 2. Utilisation du pas : un caractère sur deux
print(texte[0:6:2])     # "Pto"

# 3. Omision des bornes (équivalent à tout prendre) avec un pas de 2
print(texte[::2])       # "Pto"

# 4. Inverser une chaîne (pas négatif)
print(texte[::-1])      # "nohtyP"

```

> 💡 **À retenir :** En Python, l'élément situé à l'index de **`fin`** n'est jamais inclus dans le résultat. La longueur du résultat extrait correspond généralement à $\text{fin} - \text{début}$ (si le pas vaut $1$).

> 💡 En Python, les indices de découpage commencent à zéro et l'indice de fin spécifié est toujours exclus du résultat extrait.

---

## Expressions régulières

Les expressions régulières permettent de rechercher, valider ou extraire des motifs complexes dans des chaînes de caractères en s'appuyant sur le module standard `re`.

Le module standard **`re`** permet de manipuler les expressions régulières (Regex) en Python pour rechercher, valider ou remplacer des motifs de texte.

---

### 1. Codification des expressions régulières (les motifs clés)

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

### 2. Les 4 fonctions essentielles du module `re`

#### 1. `re.search()` : Trouver la première occurrence

Cherche le motif n'importe où dans la chaîne et renvoie un objet `Match` (ou `None`).

```python
import re

texte = "Le prix est de 49 euros."
# Cherche un ou plusieurs chiffres (\d+)
match = re.search(r"\d+", texte)

if match:
    print(match.group())  # "49"

```

#### 2. `re.findall()` : Extraire toutes les occurrences

Renvoie une liste contenant toutes les correspondances trouvées dans la chaîne.

```python
texte = "Contact : info@test.fr ou support@societe.com"
# Motif simple pour capter une adresse email
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", texte)

print(emails)  # ['info@test.fr', 'support@societe.com']

```

#### 3. `re.sub()` : Rechercher et remplacer

Remplacer un motif par un autre texte.

```python
texte = "Mon numéro est 0612345678"
# Masque les chiffres du numéro de téléphone
masque = re.sub(r"\d", "*", texte)

print(masque)  # "Mon numéro est **********"

```

#### 4. `re.match()` : Valider le début de la chaîne

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

### Exemple de synthèse

```python
import re

# Programme complet combinant gestion, formatage, slicing et expressions régulières
reference_brute = "   REF-9876-FR   "

# 1. Gestion : nettoyage des espaces superflus et mise en majuscules
reference_nette = reference_brute.strip()

# 2. Slicing : extraction de la portion numérique centrale
code_numerique = reference_nette[4:8]

# 3. Expressions régulières : validation du format global
pattern = r"^REF-\d{4}-[A-Z]{2}$"
est_conforme = bool(re.match(pattern, reference_nette))

# 4. Formatage : construction du message final avec une f-string
rapport = f"Référence : {reference_nette} | Code extrait : {code_numerique} | Conforme : {est_conforme}"
print(rapport)

```

### Exercices de fin de chapitre

1. **Exercice 1 :** Écrivez un script qui prend une chaîne de caractères contenant des espaces superflus et du texte en minuscules, puis utilisez les méthodes de gestion pour la nettoyer et la mettre entièrement en majuscules.
2. **Exercice 2 :** Déclarez une chaîne contenant un numéro de téléphone sous la forme d'une phrase, puis utilisez le slicing pour extraire les deux premiers caractères et formotez un message personnalisé à l'aide d'une f-string.
