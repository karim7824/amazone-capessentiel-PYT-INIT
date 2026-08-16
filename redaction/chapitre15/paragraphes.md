# Chapitre 15 : Programmation orientée objets

La programmation orientée objets permet de structurer un programme autour de concepts et de données modélisés sous forme de classes et d'objets. Maîtriser ces principes est indispensable pour concevoir des architectures logicielles modulaires et maintenables.
Dans ce chapitre :

* Approche de l'orienté objets


* Composition d'une classe (constructeur, méthodes et données)


* Objets et instances de classe (`self`, `super`)


* Héritage de classes et redéfinition


* Packages, imports et classes



---

## Approche de l'orienté objets

L'approche orientée objets consiste à regrouper au sein d'une même entité (la classe) les données (attributs) et les traitements (méthodes) qui leur sont associés. Cela favorise l'encapsulation et la réutilisabilité du code.

```python
# Modélisation conceptuelle d'un objet en Python
class Vehicule:
    pass

```

> 💡 Pensez vos classes comme des plans de construction permettant de donner naissance à des objets autonomes dotés de comportements spécifiques.

---

## Composition d'une classe - constructeur, méthodes et données

Une classe se compose d'un constructeur (la méthode spéciale `__init__`), de données attributaires et de méthodes pour définir les actions que l'objet peut réaliser.

```python
# Définition d'une classe avec constructeur et méthode
class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

```

> 💡 Le constructeur s'exécute automatiquement lors de l'instanciation de la classe pour initialiser l'état initial des données de l'objet.

---

## Objet et instance de class - self, super

L'instance représente un objet concret issu d'une classe. Le paramètre `self` fait référence à l'instance courante, tandis que `super()` permet d'accéder aux méthodes de la classe parente.

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

## Exemple de synthèse

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

## Exercices

1. **Exercice 1 :** Créez une classe `Livre` possédant un constructeur initialisant un titre et un auteur, ainsi qu'une méthode retournant une description textuelle de l'ouvrage.
2. **Exercice 2 :** Développez une classe fille `LivreNumerique` qui hérite de la classe `Livre` en y ajoutant un attribut supplémentaire pour la taille du fichier en mégaoctets, puis instanciez un objet de cette classe.