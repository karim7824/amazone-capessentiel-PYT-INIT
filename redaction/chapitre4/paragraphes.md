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

```python
# Affectation simple et affectation augmentée
score = 10     # Affectation simple de la valeur 10
score += 5     # Équivalent à score = score + 5

```

> 💡 L'opérateur d'affectation s'évalue de droite à gauche : la valeur ou le résultat de l'expression à droite est stocké dans la variable située à gauche.

---

## Opérateurs arithmétiques

Les opérateurs arithmétiques réalisent les calculs mathématiques usuels sur des types numériques (entiers et flottants). Ils permettent de manipuler des données quantitatives au sein des programmes.

```python
# Opérations arithmétiques de base
somme = 15 + 5      # Addition (vaut 20)
division = 10 / 4   # Division flottante (vaut 2.5)

```

> 💡 Utilisez l'opérateur modulo (`%`) pour obtenir le reste d'une division entière, ce qui est particulièrement utile pour tester la parité d'un nombre.

---

## Opérateurs relationnels

Les opérateurs relationnels comparent deux valeurs ou expressions et retournent systématiquement un résultat booléen (`True` ou `False`). Ils sont indispensables pour orienter l'exécution du code selon les conditions.

```python
# Comparaisons de valeurs
age = 18
majeur = age >= 18    # Retourne True car 18 est supérieur ou égal à 18

```

> 💡 Veillez à ne pas confondre l'opérateur d'égalité (`==`) avec l'opérateur d'affectation (`=`) pour éviter des erreurs de logique.

---

## Opérateurs logiques

Les opérateurs logiques permettent de combiner plusieurs expressions booléennes pour former des conditions complexes. Ils évaluent les relations à l'aide des opérateurs fondamentaux `and`, `or` et `not`.

```python
# Combinaison de conditions logiques
a l_ecole = True
a_ses_affaires = True
peut_partir = a_ecole and a_ses_affaires  # Vaut True si les deux conditions sont réunies

```

> 💡 Python utilise l'évaluation paresseuse (*short-circuit*) pour les opérateurs logiques : l'évaluation s'arrête dès que le résultat final est déterminé.

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

### Exercices de fin de chapitre

1. **Exercice 1 :** Écrivez un script qui initialise deux variables numériques, puis utilisez les opérateurs arithmétiques pour calculer leur somme, leur produit et le reste de leur division entière.
2. **Exercice 2 :** Déclarez une variable représentant l'âge d'un utilisateur et une autre indiquant s'il possède une autorisation. Utilisez des opérateurs relationnels et logiques pour vérifier s'il remplit les conditions d'accès (âge supérieur ou égal à 18 et autorisation vraie).
