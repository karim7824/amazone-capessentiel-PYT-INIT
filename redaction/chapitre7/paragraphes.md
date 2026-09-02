# Chapitre 5 : Manipulation des données structurées - list, dict et set

La manipulation des données structurées permet d'organiser, de stocker et de parcourir efficacement des collections d'éléments en Python. Maîtriser ces structures est indispensable pour traiter des volumes d'informations complexes.
Dans ce chapitre :

* Gestion des listes
* Gestion des dictionnaires (dict)
* Gestion des ensembles (set)

---

## Gestion des listes

Les listes permettent de stocker une collection ordonnée d'éléments modifiables. Elles autorisent les doublons et offrent de nombreuses méthodes pour ajouter, supprimer ou trier des données en mémoire.

```python
# Création et modification d'une liste
fruits = ["pomme", "banane"]
fruits.append("orange")  # Ajout d'un élément à la fin

```

> 💡 Utilisez la compréhension de liste pour filtrer ou transformer rapidement les éléments d'une liste de manière élégante et performante.

---

## Gestion des dict

Les dictionnaires stockent des données sous forme de paires clé-valeur, permettant un accès ultra-rapide aux valeurs grâce à leurs clés uniques. Ils sont parfaits pour représenter des objets ou des configurations.

```python
# Déclaration et accès dans un dictionnaire
utilisateur = {"nom": "Alice", "age": 30}
ville = utilisateur.get("ville", "Inconnue")  # Évite une erreur si la clé n'existe pas

```

> 💡 Privilégiez l'utilisation de la méthode `.get()` pour interroger un dictionnaire lorsque la clé recherchée est susceptible de ne pas y figurer.

---

## Gestion des set

Les ensembles (`set`) stockent des collections non ordonnées d'éléments uniques. Ils suppriment automatiquement les doublons et s'avèrent extrêmement utiles pour effectuer des opérations mathématiques ensemblistes (union, intersection).

```python
# Création d'un ensemble et suppression des doublons
nombres = {1, 2, 2, 3, 4}  # Le doublon '2' est automatiquement éliminé
nombres.add(5)

```

> 💡 Utilisez les opérateurs ensemblistes comme `&` pour l'intersection ou `|` pour l'union afin de comparer rapidement des collections de données.

---

## Exemple de synthèse

```python
# Programme complet combinant listes, dictionnaires et ensembles
# 1. Gestion des listes : stockage des identifiants de connexions successives
historique_connexions = ["user_1", "user_2", "user_1", "user_3"]

# 2. Gestion des set : extraction des utilisateurs uniques sans doublons
utilisateurs_uniques = set(historique_connexions)

# 3. Gestion des dict : association d'un statut à chaque utilisateur unique
statuts_utilisateurs = {
    "user_1": "actif",
    "user_2": "inactif",
    "user_3": "actif"
}

print(f"Utilisateurs uniques : {utilisateurs_uniques}")
print(f"Statut de user_1 : {statuts_utilisateurs.get('user_1')}")

```

## Exercices

1. **Exercice 1 :** Créez une liste contenant plusieurs prénoms avec des doublons, convertissez-la en ensemble (`set`) pour éliminer les doublons, puis affichez le résultat.
2. **Exercice 2 :** Déclarez un dictionnaire représentant un produit (avec les clés nom, prix et stock), puis écrivez une instruction pour mettre à jour la valeur du stock.