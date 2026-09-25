# Chapitre 9 : Les fonctions et passage d'arguments

Les fonctions permettent de modulariser le code en regroupant des instructions réutilisables sous un même nom. Maîtriser le passage d'arguments et les structures de retour est indispensable pour concevoir des programmes propres et maintenables.
Dans ce chapitre :

* Définition des fonctions, arguments, passage et valeur de retour (`return`)
* Arguments et valeurs par défaut
* Arguments variables via les tuples, `*args` et `**kwargs`
* Fonctions en tant qu'arguments (délégués)

---

## Les fonctions, arguments , passage par valeur, return

Une fonction se déclare avec le mot-clé `def` suivi d'un nom et de parenthèses. Elle accepte des arguments en entrée et peut renvoyer un résultat grâce à l'instruction `return`.

```python
# Déclaration d'une fonction simple avec retour
def additionner(a, b):
    resultat = a + b
    return resultat

# Appel
r = additionner (10,20)
print(r)

```

> 💡 En Python, les objets sont passés par affectation : modifier un objet mutable à l'intérieur d'une fonction se répercute en dehors, contrairement aux objets immuables.

---

## Arguments et valeurs par défaut

Les arguments par défaut permettent de définir une valeur de repli lorsqu'un paramètre n'est pas explicitement fourni lors de l'appel de la fonction.

```python
# Fonction avec un argument doté d'une valeur par défaut
def saluer(nom, message="Bonjour"):
    return f"{message}, {nom} !"

# Appel 
r = saluer("Karim", "Hello")
print(r) # Hello Karim
r = saluer("Karim")
print(r) Bonjour Karim
```

> 💡 Ne jamais utiliser d'objets mutables (comme des listes ou des dictionnaires) comme valeurs par défaut d'une fonction, car leur état serait conservé entre les appels successifs.

---

## Arguments en tant que tuple

Il est possible de regrouper plusieurs valeurs d'arguments dans un tuple pour les manipuler de manière globale au sein de la fonction.

```python
# Fonction acceptant un tuple d'éléments regroupés
def afficher_coordonnees(coord):
    x, y = coord
    return f"Position X: {x}, Y: {y}"

# Appel
r = afficher_coordonnees((123, 456))
print(r)
```

> 💡 Utilisez l'emballage de tuples lorsque vos données possèdent une structure fixe et ordonnée que vous souhaitez traiter en bloc.

---

## Arguments avec *args

La syntaxe `*args` permet de transmettre un nombre variable d'arguments positionnels non nommés à une fonction, qui les récupère automatiquement sous forme de tuple.

```python
# Fonction acceptant un nombre indéfini d'arguments positionnels
def sommer_tout(*args):
    return sum(args)

# Appels
r = sommer_tout(11,22)
print(r)
r = sommer_tout(11,22,33,44)
print(r)

```

> 💡 Le nom `args` est une convention en Python, mais c'est l'astérisque `*` qui indique au langage de capturer tous les arguments positionnels excédentaires.

---

## Arguments *kargs

La syntaxe `**kwargs` (souvent appelée `kargs`) permet de récupérer un nombre variable d'arguments nommés sous la forme d'un dictionnaire au sein de la fonction.

```python
# Fonction acceptant des arguments nommés dynamiques
def configurer(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle} = {valeur}")

```

> 💡 L'utilisation conjointe de `*args` et `**kwargs` offre une flexibilité maximale pour créer des fonctions enveloppes (*wrappers*) ou des décorateurs.

---

## Fonction en tant qu'argument (delegate)

En Python, les fonctions sont des objets de première classe, ce qui signifie qu'elles peuvent être passées en tant qu'arguments à d'autres fonctions, agissant ainsi comme des délégués.

```python
# Utilisation d'une fonction en tant qu'argument
def appliquer_operation(operation, x, y):
    return operation(x, y)

# lambda a, b: a * b  equivalent de def <anonyme> (a, b) : return a * b
resultat = appliquer_operation(lambda a, b: a * b, 4, 5)
print(resultat)

```

> 💡 Passer des fonctions en argument est la base de la programmation fonctionnelle et permet de concevoir des algorithmes hautement génériques et réutilisables.

---

## Exemple de synthèse

```python
# Programme complet combinant fonctions, valeurs par défaut, *args, **kwargs et délégués

def calculer_total_remise(taux=0.1, *montants, **details):
    """Calcule un total avec *args et affiche les options via **kwargs."""
    sous_total = sum(montants)
    total_net = sous_total * (1 - taux)
    
    print(f"Facture pour {details.get('client', 'Client inconnu')}")
    print(f"Sous-total : {sous_total}€ | Net : {total_net}€")
    return total_net

# Fonction déléguée à passer en paramètre
def formater_monnaie(montant):
    return f"{montant:.2f} EUR"

# Appel de la fonction principale avec différents types d'arguments
montant_final = calculer_total_remise(0.2, 100.0, 50.0, 25.0, client="Alice", mode="express")
print("Format final :", formater_monnaie(montant_final))

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez une fonction qui accepte un nombre indéfini d'entiers via `*args` et retourne leur moyenne arithmétique.

**Exercice 2 :** Créez une fonction qui prend en paramètre une fonction mathématique et deux nombres, puis applique cette fonction sur les deux nombres pour retourner le résultat.
