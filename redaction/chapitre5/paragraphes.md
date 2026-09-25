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

### Exemple de synthèse

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

### Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script qui prend une chaîne de caractères représentant un prix avec des décimales, la convertit en type `float`, lui applique une taxe de 20%, puis convertit le résultat final en `str` pour l'afficher avec un message explicite.

**Exercice 2 :** Déclarez une variable entière et une variable flottante, effectuez une addition entre les deux, puis vérifiez et affichez le type de la variable résultante pour observer la conversion implicite de Python.
