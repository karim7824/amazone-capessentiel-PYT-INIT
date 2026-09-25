# Chapitre 17 : Programmation orientée objets

La programmation orientée objets permet de structurer un programme autour de concepts et de données modélisés sous forme de classes et d'objets. Maîtriser ces principes est indispensable pour concevoir des architectures logicielles modulaires et maintenables.
Dans ce chapitre :

* Approche de l'orienté objets
* Composition d'une classe (constructeur, méthodes et données)
* Objets et instances de classe (`self`, `super`)
* Héritage de classes et redéfinition
* Packages, imports et classes

---
## Approche de l'orienté objets

L'approche orientée objets consiste à regrouper au sein d'une même entité (la classe) les données (attributs) et les traitements (méthodes) qui leur sont associés. Cela favorise l'encapsulation et la réutilisabilité du code. L'orienté objet permet de modéliser les entités métiers observées.

Les piliers de la Programmation Orientée Objet (suite)**

* **Classe :** C'est la structure fondamentale utilisée pour **encapsuler les données** (les attributs) et **les traitements** (les méthodes) associés à une même entité observée. Elle agit comme un modèle ou un plan de fabrication abstract pour tous les éléments de même nature.
* **Objet :** C'est une **instance concrète** d'une classe. À partir d'un seul plan (la classe), on peut instancier un nombre illimité d'objets distincts, chacun possédant son propre état (ses propres valeurs pour chaque attribut) tout en partageant les mêmes comportements (les méthodes).
* **Le Constructeur (`__init__`) :** Il s'agit d'une méthode spéciale exécutée **automatiquement** lors de la création de chaque objet. Son rôle principal est d'initialiser l'état initial de l'instance en lui attribuant ses valeurs de départ.
* **Le paramètre `self` :** En Python, `self` représente une **référence explicite à l'instance courante** de l'objet en cours de manipulation. Il doit être passé comme premier paramètre de toute méthode d'instance afin de pouvoir lire ou modifier les attributs propres à cet objet.
* **L'Encapsulation :** Ce principe consiste à **masquer les détails internes** d'un objet et à protéger ses données contre des modifications directes et involontaires. En Python, la protection se fait par convention d'écriture :
* Un préfixe simple `_attribut` indique un attribut **protégé** (déconseillé à l'accès direct hors de la classe).
* Un préfixe double `__attribut` active le *Name Mangling* (masquage de nom) pour rendre l'attribut **privé**.

* **L'Héritage :** C'est le mécanisme permettant à une classe dite "fille" d'**hériter des propriétés et des méthodes** d'une classe dite "mère". Cela favorise la réutilisation du code et permet d'exprimer des relations hiérarchiques (ex. *Un Chien "est un" Animal*).
* **Le Polymorphisme :** Il permet à des objets issus de classes différentes de proposer une méthode portant le même nom, mais adaptant son comportement selon la classe concernée. Cela permet de traiter différents types d'objets de manière uniforme via une interface commune.

```python
class Vehicule:  # Classe
    def __init__(self, marque: str):  # Constructeur + self
        self.marque = marque  # Attribut public
        self._vitesse = 0  # Attribut protégé (encapsulation)

    def accelerer(self):  # Méthode
        self._vitesse += 10

class Voiture(Vehicule):  # Héritage
    def accelerer(self):  # Polymorphisme (comportement spécifique)
        self._vitesse += 20


# Instanciation de plusieurs objets à partir des classes
ma_voiture = Voiture("Peugeot") 
mon_camion = Vehicule("Volvo")

ma_voiture.accelerer() 
mon_camion.accelerer()

```

> 💡 Pensez vos classes comme des plans de construction permettant de donner naissance à des objets autonomes dotés de comportements spécifiques.

---

## Objet et instance de class - self, super

L'instance représente un objet concret issu d'une classe. Le paramètre `self` fait référence à l'instance courante, tandis que `super()` permet d'accéder aux méthodes de la classe parente en cas d'héritage

```python
# Utilisation de self pour lier les données à l'instance
class Chien:
    def __init__(self, nom):
        self.nom = nom
        
    def aboyer(self):
        return f"{self.nom} aboie !"

```

> 💡 Utilisez systématiquement `self` comme premier paramètre de vos méthodes d'instance pour garantir l'accès correct aux attributs propres de l'objet.

---

## Composition d'une classe - constructeur, méthodes et données

Une classe se compose d'un constructeur (la méthode spéciale `__init__`), de données attributaires et de méthodes pour définir les actions que l'objet peut réaliser.

```python
# Définition d'une classe avec constructeur, attributs et méthodes
class CompteBancaire:
    def __init__(self, titulaire: str, solde_initial: float = 0.0):
        # Attributs (données propres à chaque objet)
        self.titulaire = titulaire
        self.solde = solde_initial

    # Méthode pour afficher les informations du compte
    def afficher_solde(self):
        print(f"Compte de {self.titulaire} : {self.solde:.2f} €")

    # Méthode pour créditer le compte (action)
    def deposer(self, montant: float):
        if montant > 0:
            self.solde += montant
            print(f"Dépôt de {montant:.2f} € effectué.")
        else:
            print("Le montant du dépôt doit être positif.")

    # Méthode pour débiter le compte (action)
    def retirer(self, montant: float):
        if 0 < montant <= self.solde:
            self.solde -= montant
            print(f"Retrait de {montant:.2f} € effectué.")
        else:
            print("Fonds insuffisants ou montant invalide.")

# --- Utilisation de la classe (Instanciation et appel des méthodes) ---

# Instanciation de deux comptes distincts
compte_alice = CompteBancaire("Alice", 1500.0)
compte_bob = CompteBancaire("Bob", 200.0)

# Manipulation des objets
compte_alice.afficher_solde()  # Compte de Alice : 1500.00 €
compte_alice.retirer(500.0)    # Retrait de 500.00 € effectué.
compte_alice.afficher_solde()  # Compte de Alice : 1000.00 €

compte_bob.deposer(150.0)      # Dépôt de 150.00 € effectué.
compte_bob.afficher_solde()    # Compte de Bob : 350.00 €

```
* **Le constructeur (`__init__`) :** initialise les deux attributs (`titulaire` et `solde`) dès la création de l'objet.
* **Les attributs (`self.titulaire`, `self.solde`) :** stockent l'état interne de chaque compte de façon indépendante.
* **Les méthodes (`deposer`, `retirer`, `afficher_solde`) :** contiennent la logique métier pour modifier ou consulter l'état du compte.
> 💡 Le constructeur s'exécute automatiquement lors de l'instanciation de la classe pour initialiser l'état initial des données de l'objet.

---

## Héritage de classes et chaînage des constructeurs

L'**héritage** permet à une classe fille (ou dérivée) d'accéder aux attributs et méthodes d'une classe mère (ou parente). Le **chaînage des constructeurs** consiste à appeler le constructeur de la classe mère depuis le constructeur de la classe fille à l'aide de la fonction intégrée `super()`. Cela garantit que la partie "parente" de l'objet est correctement initialisée avant d'y ajouter les spécificités de la classe fille.

```python
# Classe mère (Parente)
class CompteBancaire:
    def __init__(self, titulaire: str, solde_initial: float = 0.0):
        self.titulaire = titulaire
        self.solde = solde_initial

    def afficher_solde(self):
        print(f"Compte de {self.titulaire} : {self.solde:.2f} €")

    def deposer(self, montant: float):
        if montant > 0:
            self.solde += montant


# Classe fille (Hérite de CompteBancaire)
class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire: str, solde_initial: float = 0.0, taux_interet: float = 0.02):
        # Chaînage du constructeur : appel du __init__ de CompteBancaire
        super().__init__(titulaire, solde_initial)
        
        # Attribut spécifique à la classe fille
        self.taux_interet = taux_interet

    # Méthode propre à la classe fille
    def ajouter_interets(self):
        interets = self.solde * self.taux_interet
        self.solde += interets
        print(f"Intérêts ajoutés ({self.taux_interet * 100}%) : +{interets:.2f} €")


# --- Utilisation ---

# Création d'une instance de la classe fille
mon_epargne = CompteEpargne("Charlie", 1000.0, taux_interet=0.03)

# Utilisation des méthodes héritées
mon_epargne.afficher_solde()  # Compte de Charlie : 1000.00 €
mon_epargne.deposer(500.0)

# Utilisation des fonctionnalités propres à CompteEpargne
mon_epargne.ajouter_interets() # Intérêts ajoutés (3.0%) : +45.00 €
mon_epargne.afficher_solde()  # Compte de Charlie : 1545.00 €

```

---

* **Syntaxe de l'héritage :** `class ClasseFille(ClasseMere):` déclare la relation de parenté.
* **Fonction `super()` :** renvoie une référence temporaire à la classe mère pour invoquer sa méthode `__init__()` ou d'autres méthodes surchargées.
* **Réutilisation de code :** la classe fille hérite automatiquement de toutes les méthodes publiques (`deposer`, `afficher_solde`) sans avoir à les réécrire.


## Héritage de classes et redéfinition

L'héritage permet de créer une nouvelle classe (fille) à partir d'une classe existante (parente) pour réutiliser du code et redéfinir certains comportements spécifiques.

```python
# Héritage simple et spécialisation
class Animal:
    def emettre_son(self):
        return "Son générique"

class Chat(Animal):
    def emettre_son(self):
        return "Miaou"

```

> 💡 La redéfinition de méthodes (*method overriding*) permet d'adapter le comportement d'une classe fille tout en conservant la signature de la classe parente.

---

## Packages et imports et classes

L'organisation des classes au sein de modules et de packages permet de structurer les grands projets logiciels et de les importer proprement là où ils sont nécessaires.

```python
# Importation ciblée d'une classe depuis un module de package
# from mon_package.modele import CompteBancaire

```

> 💡 Veillez à regrouper les classes ayant des responsabilités métiers proches au sein d'un même module pour préserver la clarté de votre architecture.

---

### Exemple de synthèse

```python
# Programme complet combinant classes, constructeur, méthodes, self, héritage et redéfinition

class Utilisateur:
    """Classe parente représentant un utilisateur générique."""
    def __init__(self, identifiant):
        self.identifiant = identifiant

    def obtenir_profil(self):
        return f"Utilisateur ID : {self.identifiant}"

class Administrateur(Utilisateur):
    """Classe fille héritant d'Utilisateur avec redéfinition."""
    def __init__(self, identifiant, niveau_acces):
        super().__init__(identifiant)  # Appel du constructeur parent
        self.niveau_acces = niveau_acces

    def obtenir_profil(self):
        # Redéfinition de la méthode héritée
        profil_base = super().obtenir_profil()
        return f"{profil_base} | Rôle : Admin (Niveau {self.niveau_acces})"

# Instanciation et test des objets
admin = Administrateur("USR-001", 3)
print(admin.obtenir_profil())

```

## Exercices de fin de chapitre

**Exercice 1 :** Créez une classe `Livre` possédant un constructeur initialisant un titre et un auteur, ainsi qu'une méthode retournant une description textuelle de l'ouvrage.

**Exercice 2 :** Développez une classe fille `LivreNumerique` qui hérite de la classe `Livre` en y ajoutant un attribut supplémentaire pour la taille du fichier en mégaoctets, puis instanciez un objet de cette classe.
