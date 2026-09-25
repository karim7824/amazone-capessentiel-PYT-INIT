# Chapitre 18 : Accès aux bases de données

L'accès aux bases de données permet de persister, d'interroger et de structurer des volumes importants d'informations de manière sécurisée en Python. Maîtriser ces concepts est indispensable pour connecter vos applications à des systèmes de stockage relationnels.
Dans ce chapitre :

* Concepts de base des bases de données relationnelles
* Connexion et paramétrage via la connexion et le curseur
* Gestion de la structure des données avec le DDL (tables)
* Gestion des transactions et validation avec le `commit`
* Manipulation des données avec le DML (`SELECT`, `WHERE`)

---

## Concepts de base

Les bases de données relationnelles (SGBDR) permettent de stocker et d'organiser des données tabulaires structurées sous forme de **tables** composées de **lignes** (enregistrements ou n-uplets) et de **colonnes** (attributs ou champs).

Grâce aux contraintes d'intégrité et au respect des propriétés ACID (Atomicité, Cohérence, Isolation, Durabilité), elles garantissent la **cohérence des données**, la **rapidité de recherche** via des indexations optimisées et la **gestion de la concurrence d'accès** simultanée par plusieurs utilisateurs.

---

**Concepts clés**

* **Table (ou Relation) :** Structure bidimensionnelle représentant une entité du monde réel (ex. `Client`, `Commande`).
* **Clé primaire (*Primary Key*) :** Attribut unique (ex. un identifiant ou un code) permettant de distinguer chaque ligne d'une table sans ambiguïté.
* **Clé étrangère (*Foreign Key*) :** Attribut établissant un lien relationnel entre deux tables en référençant la clé primaire d'une autre table.
* **Langage SQL (*Structured Query Language*) :** Langage standardisé utilisé pour interroger et manipuler les données (via les commandes `SELECT`, `INSERT`, `UPDATE`, `DELETE`).


---

## Connexion et paramétrage - connexion, cursor

La connexion établit le pont entre l'application Python et le fichier ou serveur de base de données, tandis que le curseur sert d'intermédiaire pour exécuter les requêtes SQL.

```python
import sqlite3

# Établissement de la connexion et création du curseur
connexion = sqlite3.connect("ma_base.db")
curseur = connexion.cursor()

```

> 💡 Pensez toujours à fermer explicitement votre curseur et votre connexion à la fin des traitements pour libérer les ressources système verrouillées.

---

## Gestion de la Structure de données - Table DDL

Le langage de définition de données (DDL) permet de créer, modifier ou supprimer la structure des tables au sein de la base de données (instructions `CREATE TABLE`, etc.).

```python
# Création d'une table relationnelle via une requête DDL
curseur.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        age INTEGER
    )
""")

```

> 💡 Définissez rigoureusement les types de données et les contraintes (`NOT NULL`, `PRIMARY KEY`) dès la conception de vos tables pour garantir l'intégrité des informations.

---

## Gestion des transactions - commit

La gestion des transactions permet de valider définitivement un ensemble d'opérations en base de données grâce à l'instruction `commit`, garantissant la cohérence globale des données.

```python
# Validation des modifications apportées à la base de données
connexion.commit()

```

> 💡 En cas d'erreur lors d'une transaction, utilisez l'instruction `rollback` pour annuler les modifications en cours et rétablir l'état stable précédent de la base.

---

## Manipulation des données - Select/Where DML

Le langage de manipulation des données (DML) permet d'insérer, de modifier, de supprimer et de rechercher des enregistrements à l'aide des instructions `SELECT` et de la clause `WHERE`.

```python
# Requête DML pour sélectionner des enregistrements filtrés
curseur.execute("SELECT nom, age FROM utilisateurs WHERE age >= ?", (18,))
resultats = curseur.fetchall()

```

> 💡 Utilisez toujours des requêtes paramétrées (avec des points d'interrogation `?`) pour injecter des variables afin de vous prémunir totalement contre les failles d'injection SQL.

---

### Exemple de synthèse

```python
import sqlite3

def gerer_base_de_donnees():
    """Programme complet combinant connexion, DDL, transactions et requêtes DML."""
    # 1. Connexion et paramétrage
    connexion = sqlite3.connect("entreprise.db")
    curseur = connexion.cursor()
    
    # 2. Gestion de la structure de données (DDL)
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS employes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            salaire REAL
        )
    """)
    
    # 3. Insertion de données (DML) et gestion des transactions (commit)
    curseur.execute("INSERT INTO employes (nom, salaire) VALUES (?, ?)", ("Alice", 2500.0))
    curseur.execute("INSERT INTO employes (nom, salaire) VALUES (?, ?)", ("Bob", 3100.0))
    connexion.commit()  # Validation de la transaction
    
    # 4. Manipulation des données avec SELECT et WHERE (DML)
    curseur.execute("SELECT nom, salaire FROM employes WHERE salaire > ?", (2800.0,))
    recrutements_hauts = curseur.fetchall()
    
    for employe in recrutements_hauts:
        print(f"Employé qualifié : {employe[0]} avec un salaire de {employe[1]}€")
        
    # Fermeture propre des ressources
    curseur.close()
    connexion.close()

# Exécution de la fonction de synthèse
gerer_base_de_donnees()

```

## Exercices

1. **Exercice 1 :** Écrivez un script Python qui utilise le module `sqlite3` pour créer une base de données, instancier une table `produits` (contenant un ID, un nom et un prix), puis y insérer un enregistrement validé par un `commit`.
2. **Exercice 2 :** Rédigez une requête `SELECT` associée à une clause `WHERE` pour récupérer et afficher tous les produits dont le prix est inférieur à un certain seuil depuis la table créée à l'exercice précédent.
