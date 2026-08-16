# Chapitre 8 : Traiter une masse de données

Le traitement de masses de données permet d'appliquer des transformations et des filtres performants sur des collections en Python. Maîtriser ces outils fonctionnels est indispensable pour manipuler efficacement des flux d'informations importants.
Dans ce chapitre :

* Fonctions anonymes `lambda`

* Filtrage de données avec `filter`

* Transformation de données avec `map`

* Agrégation de données avec `reduce`


---

## Fonction anonyme Lambda

Une fonction anonyme, introduite par le mot-clé `lambda`, permet de définir rapidement une fonction compacte sans nom sur une seule ligne de code. Elle est idéale pour des traitements courts et ponctuels.

```python
# Déclaration et appel d'une fonction lambda pour calculer le carré
carre = lambda x: x ** 2
resultat = carre(5)

```

> 💡 Utilisez les fonctions `lambda` principalement comme arguments pour des fonctions de traitement de collections comme `map` ou `filter`.

---

## Traitement avec filter

La fonction `filter()` permet de filtrer les éléments d'une collection en évaluant chaque élément à l'aide d'une fonction conditionnelle qui retourne un booléen.

```python
# Filtrage des nombres pairs d'une liste
nombres = [1, 2, 3, 4, 5, 6]
pairs = list(filter(lambda x: x % 2 == 0, nombres))

```

> 💡 Le résultat retourné par `filter()` en Python est un itérateur, pensez à le convertir explicitement en `list` ou `tuple` pour exploiter les données.

---

## Traitement avec map

La fonction `map()` applique une fonction spécifique à l'ensemble des éléments d'une collection itérable, transformant ainsi les données en une seule passe.

```python
# Application d'une transformation pour multiplier par 2 chaque élément
valeurs = [1, 2, 3, 4]
doubles = list(map(lambda x: x * 2, valeurs))

```

> 💡 Les compréhensions de listes constituent souvent une alternative plus lisible et idiomatique aux fonctions `map()` en Python.

---

## Traitement avec reduce

La fonction `reduce()`, issue du module `functools`, permet de réduire une collection de données à une valeur unique en appliquant cumulativement une fonction binaire de manière séquentielle.

```python
from functools import reduce

# Calcul de la somme des éléments d'une liste par réduction
nombres = [1, 2, 3, 4]
somme_totale = reduce(lambda x, y: x + y, nombres)

```

> 💡 Pensez à importer `reduce` depuis le module `functools` avant de l'utiliser, car cette fonction n'est plus intégrée directement dans l'espace de noms global de Python.

---

## Exemple de synthèse

```python
from functools import reduce

# Programme complet combinant lambda, filter, map et reduce sur une masse de données
prix_articles = [12.5, 45.0, 8.0, 100.0, 32.5]

# 1. Filtrer les articles dont le prix est supérieur à 15.0 via filter et lambda
articles_cibles = list(filter(lambda p: p > 15.0, prix_articles))

# 2. Appliquer une remise de 10% sur ces articles via map et lambda
prix_remises = list(map(lambda p: p * 0.9, articles_cibles))

# 3. Calculer le montant total cumulé de ces articles via reduce et lambda
montant_global = reduce(lambda total, p: total + p, prix_remises, 0.0)

print(f"Articles remisés : {prix_remises}")
print(f"Montant global de la commande : {montant_global:.2f} €")

```

## Exercices

1. **Exercice 1 :** Utilisez la fonction `filter()` associée à une expression `lambda` pour extraire uniquement les mots de longueur supérieure à 5 caractères d'une liste de chaînes.
2. **Exercice 2 :** Importez `reduce` depuis `functools` et écrivez un script qui calcule le produit de tous les éléments d'une liste d'entiers.