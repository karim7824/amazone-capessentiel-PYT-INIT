# Chapitre 1 : Définir et manipuler des données types en mémoire

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

```python
temperature = 23.5    # Flottant (float) pour les décimaux
est_valide = True     # Booléen (bool) valant True ou False

```

> 💡 Utilisez toujours des noms explicites pour vos variables scalaires afin d'améliorer la lisibilité immédiate du code par l'équipe projet.

---

## Types de données aggrégés - list, tuple, dict, set

Les types agrégés permettent de regrouper plusieurs valeurs au sein d'une seule structure de données en mémoire. Leur choix dépend de la nécessité d'ordre, de modification ou d'unicité des éléments.

```python
utilisateurs = ["Alice", "Bob", "Charlie"]  # Liste modifiable (list)
coordonnees = (10.0, 20.0)                  # Tuple immuable (tuple)

```

> 💡 Privilégiez les tuples pour des données fixes qui ne doivent pas être altérées au cours de l'exécution du programme, garantissant ainsi l'intégrité des structures.

---

## Valeurs littérales

Une valeur littérale correspond à la représentation directe d'une donnée constante inscrite textuellement dans le code source du programme. Elle permet d'assigner des valeurs figées sans calcul préalable.

```python
seuil_maximal = 100        # 100 est une valeur littérale entière
message_erreur = "Erreur 404"  # La chaîne est une valeur littérale textuelle

```

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

## Exemple de synthèse

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

## Exercices

1. **Exercice 1 :** Écrivez un script qui déclare quatre variables de types scalaires différents (`int`, `float`, `bool`, `str`), puis affichez le type de chacune d'elles à l'aide de la fonction `type()`.
2. **Exercice 2 :** Créez une liste contenant les notes d'un étudiant, écrivez une fonction qui calcule la moyenne de ces notes, et stockez le résultat dans une variable locale avant de le retourner.