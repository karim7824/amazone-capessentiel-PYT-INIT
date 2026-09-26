# Chapitre 20 : Les tests unitaires avec `unittest`

Garantir la fiabilité d'un code avant son déploiement est une étape indispensable du développement logiciel. Dans ce chapitre, vous découvrirez comment concevoir des tests unitaires automatisés pour vérifier le bon fonctionnement de vos fonctions et classes. L'objectif est d'acquérir les réflexes méthodologiques et d'utiliser les outils standards pour livrer des projets Python robustes et maintenables.

* L'intérêt des tests unitaires et les terminologies fondamentales (*assertion*, *fixture*, *suite*)
* L'utilisation du module standard `unittest`
* L'écriture d'une suite de tests complète sur un cas pratique (`Calcul`)
* La mesure de la couverture de code avec l'outil `coverage.py`

---

## Nécessité du test et concepts fondamentaux

Tester un programme permet d'identifier les bugs avant la mise en production et d'éviter les régressions lors de l'ajout de nouvelles fonctionnalités. Un **test unitaire** isole la plus petite unité de code possible (généralement une fonction ou une méthode) pour en vérifier le comportement face à des entrées données.

Plusieurs concepts clés structurent l'écriture des tests :

* **Assertion** : une vérification logique qui valide si le résultat obtenu correspond au résultat attendu.
* **Fixture** : la mise en place d'un environnement contrôlé (variables, instances, connexions) avant l'exécution du test, puis son nettoyage après.
* **Suite de tests** : un regroupement de plusieurs cas de tests exécutés ensemble.

```python
# Exemple d'assertion basique en Python pur sans framework
def additionner(a, b):
    return a + b

# Vérification manuelle (lève une AssertionError si le résultat est incorrect)
assert additionner(2, 3) == 5, "L'addition de 2 et 3 doit valoir 5"

```

> Un bon test unitaire doit être **I.S.O.L.É.** : Indépendant, Saisissable (lisible), Automatique, Répétable et Rapide. Un test ne doit jamais dépendre de l'exécution d'un autre test.

---

## Prise en main du framework standard `unittest`

Python intègre nativement le module `unittest`, inspiré du framework *JUnit*. Il fournit une structure orientée objet basée sur la classe `unittest.TestCase`.

Pour créer un cas de test, il suffit de dériver de `unittest.TestCase` et de concevoir des méthodes dont le nom commence obligatoirement par le préfixe `test_`.

Module à tester : parite.py
```python
def est_pair(nombre):
    """Retourne True si le nombre est pair, False sinon."""
    return nombre % 2 == 0
```

Module de teste : parite.test.py
```python
import unittest

# TestEstPair prend ses fonctionnalités oar héritage de unittest.TestCase
class TestEstPair(unittest.TestCase):

	# obligation de prefixer avec test_<nom methode>
    def test_nombre_pair(self):
        self.assertTrue(est_pair(4))

	# obligation de prefixer avec test_<nom methode>
    def test_nombre_impair(self):
        self.assertFalse(est_pair(7))

if __name__ == '__main__':
    unittest.main()

```

Il y a une grande librairies d'assertion mais voici les plus fréquentes fournies par `unittest.TestCase`:

* `assertEqual(a, b)` : vérifie que `a == b`
* `assertNotEqual(a, b)` : vérifie que `a != b`
* `assertTrue(x)` / `assertFalse(x)` : vérifie l'état booléen de `x`
* `assertRaises(Exception)` : vérifie qu'une exception spécifique est bien levée

---

## tester la classe Calcul

Appliquons la démarche sur une classe métier `Calcul` gérant des opérations arithmétiques et des cas limites (division par zéro).

**Implémentation de la classe à tester**

```python
# fichier: calcul.py

class Calcul:
    """Classe fournissant des opérations mathématiques de base."""
    
    def additionner(self, a, b):
        return a + b

    def diviser(self, a, b):
        if b == 0:
            raise ValueError("La division par zéro est impossible.")
        return a / b

```

**Écriture du fichier de test**

Nous utilisons `setUp()` pour instancier la classe `Calcul` avant chaque test.

```python
# fichier: test_calcul.py
import unittest
from calcul import Calcul

class TestCalcul(unittest.TestCase):

    def setUp(self):
        """Fixture : exécutée automatiquement avant chaque méthode de test."""
        self.calculateur = Calcul()

    def test_additionner(self):
        resultat = self.calculateur.additionner(10, 5)
        self.assertEqual(resultat, 15)

    def test_diviser_valeurs_valides(self):
        resultat = self.calculateur.diviser(10, 2)
        self.assertEqual(resultat, 5.0)

    def test_diviser_par_zero(self):
        """Vérifie que la division par zéro lève bien une ValueError."""
        with self.assertRaises(ValueError):
            self.calculateur.diviser(10, 0)

if __name__ == '__main__':
    unittest.main()

```

**Pour exécuter cette suite de tests depuis votre terminal **

```bash
python -m unittest test_calcul.py

```


> ⚠️ **Piège**
> N'oubliez pas le préfixe `test_` devant le nom de vos méthodes dans la classe de test. Tout méthode sans ce préfixe sera ignorée par le moteur de `unittest`.

---

## Mesure de la couverture de code (*Code Coverage*)

La **couverture de code** mesure le pourcentage de lignes de code métier exécutées lors du lancement des tests unitaires. Elle permet de repérer les zones de code oubliées ou non testées (comme des branches conditionnelles `if/else` spécifiques).

En Python, l'outil le plus répandu est la bibliothèque `coverage`.

## Installation et utilisation

**Installation via pip :**

```bash
pip install coverage

```

**Exécution des tests sous le contrôle de coverage :**

```bash
coverage run -m unittest test_calcul.py

```

**Affichage du rapport dans la console :**

```bash
coverage report -m

```

L'option `-m` (missing) indique les numéros des lignes qui n'ont pas été couvertes lors des tests.

**Génération d'un rapport HTML détaillé :**

```bash
coverage html

```

Cette commande crée un dossier `htmlcov/` contenant une interface web permettant de visualiser ligne par ligne le code couvert et non couvert.

> 💡 **Note**
> Viser 100 % de couverture est une bonne ambition, mais une couverture élevée ne garantit pas l'absence totale de bugs. La qualité des jeux de données et des assertions reste prédominante.

---

## Exercices de fin de chapitre

Dans ce chapitre, vous avez appris à structurer vos tests unitaires grâce au module `unittest`, à automatiser la vérification de vos fonctions et à valider la levée d'exceptions. Vous avez également vu comment quantifier l'efficacité de votre suite de tests avec l'outil de métrique `coverage.py`.

**Exercice 1 : teste une fonction `def aleatoire`**
Pour une fonction aleatoire basée sur random.randint(), valider le fait que sur 100 tirages de valeurs comprises dans l'interval [0,20], il y a autant de valeur paires que de valeur impairs

**Exercice 2 : teste une dans une `class Aleatoire`**
Pour une classe contenant la fonction aleatoire basée sur random.randint(), valider le fait que sur 100 tirages de valeurs comprises dans l'interval [0,20], il y a autant de valeur paires que de valeur impairs
Générez le rapport `coverage` pour vérifier que 100 % de la classe `Aleatoire` est couverte.
