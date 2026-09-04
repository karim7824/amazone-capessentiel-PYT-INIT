# Chapitre 8 : Les instructions contrôles

Les instructions de contrôle permettent d'orienter le flux d'exécution d'un programme en fonction de conditions et de répéter des blocs de instructions. Maîtriser ces structures est indispensable pour automatiser des tâches complexes.
Dans ce chapitre :

* Structures conditionnelles `if`/`else` et `match`
* Boucles itératives (`for`/`else`, `while`)
* Itérations avancées (`range`, `zip`, `items()`)

---

## Structure conditionnelles if/else/then,match

Les structures conditionnelles permettent d'exécuter des blocs de code différents selon la validité d'une ou plusieurs conditions logiques. L'instruction `match`, introduite récemment, facilite les aiguillages complexes par motif.

Voici la forme générale des structures conditionnelles `if / elif / else` en Python :

### Forme générale

```python
if condition_1:
    # Bloc exécuté si condition_1 est True
    instructions
elif condition_2:
    # Bloc exécuté si condition_1 est False ET condition_2 est True
    instructions
elif condition_3:
    # Autre condition optionnelle...
    instructions
else:
    # Bloc exécuté si AUCUNE des conditions précédentes n'est True
    instructions

```

---

### Points clés à retenir

* **`if`** : Obligatoire (un seul par bloc). C'est le point d'entrée de la condition.
* **`elif`** *(contraction de "else if")* : Optionnel. Il peut y en avoir zéro, un ou plusieurs à la suite.
* **`else`** : Optionnel (un seul à la fin). Il capture tous les cas restants.
* **Les deux-points `:**` : Indispensables après chaque clause (`if`, `elif`, `else`).
* **L'indentation** *(4 espaces)* : Obligatoire. C'est elle qui délimite le bloc de code rattaché à chaque condition.

---

### Exemple concret

```python
note = 14

if note >= 16:
    print("Mention Très Bien")
elif note >= 14:
    print("Mention Bien")
elif note >= 12:
    print("Mention Assez Bien")
elif note >= 10:
    print("Admis")
else:
    print("Ajourné")

```

> 💡 **Variante (Forme condensée / Opérateur ternaire) :**
> Pour une affectation simple selon une seule condition, vous pouvez écrire :
> `statut = "Majeur" if age >= 18 else "Mineur"`

---

## Structure match

L'instruction `match` réalise un filtrage par motif (*pattern matching*), permettant de comparer une valeur à plusieurs structures ou cas possibles de manière très lisible.

```python
# Utilisation de match pour aiguiller selon une commande
commande = "quit"
match commande:
    case "start":
        print("Démarrage...")
    case "quit":
        print("Arrêt...")
    case _:
        print("Commande inconnue")

```

> 💡 Utilisez le motif universel `_` comme dernier cas dans un `match` pour capturer toutes les valeurs non gérées explicitement.

---

## Boucles - for/else

La boucle `for` permet de parcourir séquentiellement les éléments d'une collection. En Python, elle peut être associée à un bloc `else` optionnel qui s'exécute si la boucle s'est terminée sans interruption par un `break`.

```python
# Parcours d'une liste avec une boucle for
nombres = [1, 2, 3]
for n in nombres:
    print(n)

```

> 💡 Utilisez le bloc `else` d'une boucle `for` pour exécuter du code de validation si aucun élément recherché n'a déclenché de rupture anticipée.

---

## Boucles - while

La boucle `while` répète l'exécution d'un bloc d'instructions tant qu'une condition booléenne associée reste évaluée à `True`. Elle est idéale lorsque le nombre d'itérations n'est pas connu à l'avance.

```python
# Compteur avec une boucle while
compteur = 0
while compteur < 3:
    print(compteur)
    compteur += 1

```

> 💡 Veillez à toujours faire évoluer la variable de condition à l'intérieur d'une boucle `while` pour éviter les boucles infinies.

---

## Boucles - avec range

L'association d'une boucle `for` avec la fonction `range()` permet de répéter un bloc d'instructions un nombre précis de fois en générant une séquence numérique efficace.

```python
# Répétition d'une action à l'aide de range
for i in range(3):
    print(f"Itération numéro {i}")

```

> 💡 La fonction `range(debut, fin, pas)` accepte des arguments optionnels pour démarrer à un autre indice ou parcourir les éléments par pas spécifiques.

---

## Boucles - avec zip

La fonction `zip()` permet de parcourir simultanément plusieurs collections en assemblant leurs éléments sous forme de tuples, ce qui simplifie le traitement croisé de données.

```python
# Itération conjointe sur deux listes
noms = ["Alice", "Bob"]
scores = [85, 92]
for nom, score in zip(noms, scores):
    print(f"{nom} a obtenu {score} points")

```

> 💡 Si les collections passées à `zip()` n'ont pas la même longueur, l'itération s'arrête automatiquement dès que la plus courte est épuisée.

---

## Boucles - avec items() pour les dictionnaires

La méthode `.items()` permet de parcourir à la fois les clés et les valeurs d'un dictionnaire lors d'une même boucle `for`, optimisant la lecture des données structurées.

```python
# Parcours des clés et valeurs d'un dictionnaire
parametres = {"theme": "sombre", "volume": 80}
for cle, valeur in parametres.items():
    print(f"{cle} : {valeur}")

```

> 💡 Utilisez `.items()` dès que vous avez besoin de manipuler simultanément la clé et sa valeur associée pour éviter des appels d'accès superflus.

---

## Exemple de synthèse

```python
# Programme complet combinant conditions, boucles, range, zip et items
utilisateurs = ["Alice", "Bob", "Charlie"]
points = [45, 60, 30]

# 1. Boucle avec range pour un affichage numéroté
for i in range(len(utilisateurs)):
    print(f"Rang {i + 1}")

# 2. Boucle avec zip pour associer utilisateurs et scores
for user, score in zip(utilisateurs, points):
    # 3. Structure conditionnelle classique
    if score >= 50:
        niveau = "Expert"
    else:
        niveau = "Débutant"
    print(f"{user} ({niveau}) avec {score} pts")

# 4. Boucle avec items() pour parcourir un dictionnaire de configuration
config = {"mode": "admin", "debug": True}
for parametre, etat in config.items():
    match parametre:
        case "mode":
            print(f"Mode actif : {etat}")
        case "debug":
            print(f"Mode débogage activé : {etat}")

```

### Exercices de fin de chapitre

1. **Exercice 1 :** Écrivez un script qui produit, au moyen d'une boucle, une liste de 5 listes  = [['TOTO1',1],['TOTO2',2],...['TOTO5',5]]. Ensuite pourcourir cette liste et afficher que le noms TOTO1, TOTO2...
2. **Exercice 2 :** Écrivez un script qui produit, au moyen d'une boucle, une liste de 5 dict  = [{'nom':'TOTO1','age' : 1},...{'nom':'TOTO5','age' : 5}]. Ensuite pourcourir cette liste et afficher que le noms TOTO1, TOTO2...
3. **Exercice 2 :** Créez un dictionnaire associant des noms de fruits à leur prix, puis utilisez la méthode `.items()` dans une boucle pour afficher chaque fruit et son prix avec une structure conditionnelle vérifiant s'il est supérieur à un certain seuil.
