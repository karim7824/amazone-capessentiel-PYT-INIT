# Chapitre 11 : Les générateurs

Les générateurs permettent de produire des séquences de valeurs à la demande sans stocker l'intégralité des données en mémoire. Maîtriser ces concepts est indispensable pour optimiser l'efficacité de vos programmes lors du traitement de grands volumes d'informations.
Dans ce chapitre :

* Boucle et instruction `yield`
* Générateurs prédéfinis

---

## Boucle et instruction yield

L'instruction `yield` permet à une fonction de retourner une valeur tout en suspendant son état d'exécution, transformant ainsi la fonction en un générateur capable de reprendre là où il s'était arrêté.

```python
# Définition d'une fonction génératrice simple
def generer_nombres(limite):
    n = 0
    while n < limite:
        yield n
        n += 1

print ( generer_nombres) # <function generer_nombres at 0x000001700E078E00>
list( generer_nombres(5)) # [0, 1, 2, 3, 4]

# itération sur le générateur
for i in generer_nombres(5): print (i)  # 0 1 2 3 4

# opérateur next() et détection de StopIteration
g = generer_nombres(3)
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
print(next(g))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

```

> 💡 Contrairement à `return`, l'instruction `yield` conserve l'état local de la fonction entre chaque itération, ce qui économise considérablement la mémoire vive.

---

## Générateur prédéfinis

Les générateurs prédéfinis englobent les expressions génératrices et les structures intégrées de Python qui produisent des flux d'éléments de manière paresseuse, évitant l'allocation préalable d'une collection complète.

```python
# Utilisation d'une expression génératrice pour un calcul optimisé en mémoire
carres_gen = (x ** 2 for x in range(5))
premier_element = next(carres_gen)

```

> 💡 Privilégiez les expressions génératrices entre parenthèses plutôt que les compréhensions de listes dès que vous manipulez des flux volumineux dont vous n'avez pas besoin de stocker l'ensemble des résultats simultanément.

---

## Exemple de synthèse

```python
# Programme complet combinant la création d'un générateur avec yield et un générateur prédéfini

def lecteur_lignes_simule(donnees):
    """Générateur personnalisé pour traiter des lignes de texte à la demande."""
    for ligne in donnees:
        # Instruction yield pour suspendre et renvoyer la ligne nettoyée
        yield ligne.strip().upper()

flux_brut = ["  premiere ligne  ", "  seconde ligne  ", "  troisieme ligne  "]

# Utilisation du générateur personnalisé
gen_personnalise = lecteur_lignes_simule(flux_brut)

# Utilisation d'un générateur prédéfini (enumerate) associé
for index, texte_traite in enumerate(gen_personnalise, start=1):
    print(f"Ligne {index} : {texte_traite}")

```

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez une fonction génératrice utilisant `yield` pour produire les nombres pairs jusqu'à une limite passée en paramètre, puis parcourez ce générateur avec une boucle `for`.

**Exercice 2 :** Créez une expression génératrice qui calcule les carrés des nombres de 1 à 10, et récupérez les valeurs un par un à l'aide de la fonction `next()`.
