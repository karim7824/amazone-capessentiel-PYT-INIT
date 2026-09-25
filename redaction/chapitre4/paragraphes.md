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
