# Chapitre 19 : Accès aux bases de données

L'accès aux bases de données permet de persister, d'interroger et de structurer des volumes importants d'informations de manière sécurisée en Python. Maîtriser ces concepts est indispensable pour connecter vos applications à des systèmes de stockage relationnels.
Dans ce chapitre :

* Concepts de base des bases de données relationnelles
* Connexion et paramétrage via la connexion et le curseur
* Gestion de la Structure de données - requêtes DDL
* Manipulation des données - requêtes DML
* Gestion des transactions — commit et rollback
* Bonne pratique : Gestion sécurisée des connexions

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

En Python, la norme **DB-API 2.0** définit une interface standardisée pour interagir avec les bases de données. Le module intégré **`sqlite3`** permet d'exploiter une base de données relationnelle légère et serveur-less sans nécessiter de configuration externe complexifiée.

```python
import sqlite3

# Connexion à la base de données (fichier local ou en mémoire via ':memory:')
connexion = sqlite3.connect("ma_banque.db")

# Création d'un curseur pour exécuter les requêtes SQL
curseur = connexion.cursor()

# Création d'une table avec clés et contraintes
curseur.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

```

> 💡 Pensez toujours à fermer explicitement votre curseur et votre connexion à la fin des traitements pour libérer les ressources système verrouillées.

---

## Gestion de la Structure de données - requêtes DDL

Le langage de définition de données (DDL) permet de créer, modifier ou supprimer la structure des tables au sein de la base de données (instructions `CREATE TABLE`, etc.).

Les opérations qui portent sur la structure des tables sont : DDL (CREATE, ALTER, DROP, TRUNCATE) 

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

## Manipulation des données - requêtes DML

Le langage de manipulation des données (DML) permet d'insérer, de modifier, de supprimer et de rechercher des enregistrements à l'aide des instructions `SELECT` et de la clause `WHERE`.

Les opérations qui portent sur les données des tables sont : DML (SELECT, INSERT, UPDATE, DELETE) 

Voici plusieurs exemples concrets d'opérations **DML** (*Data Manipulation Language*) en Python avec `sqlite3`, illustrant les différentes façons d'insérer, lire, mettre à jour et supprimer des données.

---

**Insertion d'une seule ligne**

```python
# Insertion simple avec passage de paramètres sous forme de tuple
nouvel_utilisateur = ("Alice", 25, "alice@example.com")
curseur.execute(
    "INSERT INTO utilisateurs (nom, age, email) VALUES (?, ?, ?)",
    nouvel_utilisateur
)
connexion.commit()

```

**Insertion multiple en masse (`executemany`)**

```python
# Liste de tuples pour insérer plusieurs lignes en une seule opération
plusieurs_utilisateurs = [
    ("Bob", 17, "bob@example.com"),
    ("Charlie", 30, "charlie@example.com"),
    ("Diana", 22, "diana@example.com")
]
curseur.executemany(
    "INSERT INTO utilisateurs (nom, age, email) VALUES (?, ?, ?)",
    plusieurs_utilisateurs
)
connexion.commit()

```

---

**Récupérer un seul enregistrement (`fetchone`)**

```python
# Utile quand on recherche par identifiant unique ou clé primaire
curseur.execute("SELECT * FROM utilisateurs WHERE email = ?", ("alice@example.com",))
utilisateur = curseur.fetchone()

if utilisateur:
    print(f"Trouvé : {utilisateur}")  # Retourne un tuple : (1, 'Alice', 25, 'alice@example.com')

```

**Récupérer un nombre limité d'enregistrements (`fetchmany`)**

```python
# Récupère uniquement les 2 premiers résultats
curseur.execute("SELECT nom, age FROM utilisateurs ORDER BY age DESC")
top_2 = curseur.fetchmany(2)
print("Les 2 plus âgés :", top_2)

```

**Filtrage complexe avec tris et limites**

```python
# Recherche multi-critères
sql = """
SELECT nom, age 
FROM utilisateurs 
WHERE age >= ? AND nom LIKE ? 
ORDER BY nom ASC 
LIMIT ?
"""
curseur.execute(sql, (18, "A%", 10))  # Majeurs dont le nom commence par 'A', max 10
resultats = curseur.fetchall()

```

---

**Modification de données (`UPDATE`)**

```python
# Mise à jour du champ 'age' pour un utilisateur spécifique
nouvel_age = 26
email_cible = "alice@example.com"

curseur.execute(
    "UPDATE utilisateurs SET age = ? WHERE email = ?",
    (nouvel_age, email_cible)
)
connexion.commit()

# Afficher le nombre de lignes modifiées
print(f"Lignes modifiées : {curseur.rowcount}")

```

---

**Suppression de données (`DELETE`)**

```python
# Suppression des utilisateurs mineurs
age_limite = 18

curseur.execute("DELETE FROM utilisateurs WHERE age < ?", (age_limite,))
connexion.commit()

print(f"Utilisateurs supprimés : {curseur.rowcount}")

```

---

**Synthèse des méthodes de récupération (`fetch`)**

| Méthode | Comportement | Retour si aucun résultat |
| --- | --- | --- |
| **`curseur.fetchone()`** | Retourne la **première ligne** sous forme de tuple. | `None` |
| **`curseur.fetchall()`** | Retourne **toutes les lignes** sous forme d'une liste de tuples. | `[]` *(liste vide)* |
| **`curseur.fetchmany(size)`** | Retourne **au maximum `size` lignes** sous forme de liste. | `[]` *(liste vide)* |

> 💡 Utilisez toujours des requêtes paramétrées (avec des points d'interrogation `?`) pour injecter des variables afin de vous prémunir totalement contre les failles d'injection SQL.

---
## Gestion des transactions — commit et rollback

La gestion des transactions permet de valider définitivement un ensemble d'opérations en base de données grâce à l'instruction `commit`, garantissant la cohérence globale des données.

```python
import sqlite3

connexion = sqlite3.connect("banque.db")
curseur = connexion.cursor()

# Exemple de transfert d'argent entre deux comptes (Opération atomique)
compte_source = 1
compte_dest = 2
montant = 150.0

try:
    # 1. Débit du compte source
    curseur.execute(
        "UPDATE comptes SET solde = solde - ? WHERE id = ?",
        (montant, compte_source)
    )

    # 2. Crédit du compte destinataire
    curseur.execute(
        "UPDATE comptes SET solde = solde + ? WHERE id = ?",
        (montant, compte_dest)
    )

    # Validation définitive de l'ensemble des modifications
    connexion.commit()
    print("Transaction réussie et validée en base de données.")

except sqlite3.Error as e:
    # En cas d'erreur SQL, annulation de TOUTES les modifications de la transaction
    connexion.rollback()
    print(f"Erreur lors de la transaction. Modifications annulées : {e}")

finally:
    connexion.close()

```

> 💡 En cas d'erreur lors d'une transaction, utilisez l'instruction `rollback` pour annuler les modifications en cours et rétablir l'état stable précédent de la base.

---
--- 
## Bonne pratique : Gestion sécurisée des connexions

Pour éviter les fuites de mémoire et garantir la fermeture automatique des ressources même en cas d'erreur, utilisez un gestionnaire de contexte (`with`) :

```python
import sqlite3

# Le gestionnaire de contexte gère le commit/rollback automatiquement
with sqlite3.connect("ma_banque.db") as connexion:
    curseur = connexion.cursor()
    curseur.execute("SELECT COUNT(*) FROM clients")
    total = curseur.fetchone()[0]
    print(f"Nombre total de clients : {total}")
# La connexion se ferme proprement en sortant du bloc with

```
---

**Alternative moderne : Le gestionnaire de contexte (`with`)**

En Python, le gestionnaire de contexte gère les transactions automatiquement : il effectue un `commit()` si le bloc s'exécute sans erreur, ou un `rollback()` si une exception est levée.

```python
import sqlite3

connexion = sqlite3.connect("banque.db")

# Le bloc 'with connexion:' gère automatiquement la transaction (commit/rollback)
try:
    with connexion:
        connexion.execute("UPDATE comptes SET solde = solde - 100 WHERE id = 1")
        connexion.execute("UPDATE comptes SET solde = solde + 100 WHERE id = 2")
    print("Transaction validée automatiquement.")
except sqlite3.Error:
    print("Erreur détectée : rollback automatique effectué.")

```
---
---

## Exemple de synthèse

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

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script Python qui utilise le module `sqlite3` pour créer une base de données, instancier une table `produits` (contenant un ID, un nom et un prix), puis y insérer un enregistrement validé par un `commit`.

**Exercice 2 :** Rédigez une requête `SELECT` associée à une clause `WHERE` pour récupérer et afficher tous les produits dont le prix est inférieur à un certain seuil depuis la table créée à l'exercice précédent.
