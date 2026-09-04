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

---

## Conversions implicites vs explicites

Python réalise parfois des conversions implicites automatiques sans intervention du développeur pour éviter les pertes de données, tandis que les conversions explicites exigent l'appel direct à des fonctions dédiées comme `int()`, `float()` ou `str()`.

```python
# Conversion implicite d'un entier en flottant lors d'une opération mixte
resultat = 3 + 4.5  # L'entier 3 est converti implicitement en 3.0 (résultat : 7.5)

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

1. **Exercice 1 :** Écrivez un script qui prend une chaîne de caractères représentant un prix avec des décimales, la convertit en type `float`, lui applique une taxe de 20%, puis convertit le résultat final en `str` pour l'afficher avec un message explicite.
2. **Exercice 2 :** Déclarez une variable entière et une variable flottante, effectuez une addition entre les deux, puis vérifiez et affichez le type de la variable résultante pour observer la conversion implicite de Python.
