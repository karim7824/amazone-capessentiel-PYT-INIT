# L'essentiel de l'essentiel à retenir sur Python

## Installation & commandes

```bash
python --version                     # vérifier la version de Python
python -m venv .venv                 # créer un environnement virtuel
source .venv/bin/activate            # activer venv (Linux/macOS)
.venv\Scripts\activate               # activer venv (Windows)
deactivate                           # désactiver l'environnement virtuel
pip install package                  # installer un paquet
pip freeze > requirements.txt        # geler les dépendances
pip install -r requirements.txt      # installer les dépendances
python main.py                       # exécuter un script Python
python -m pytest                     # exécuter les tests unitaires
python -m pytest --cov               # couverture de code

```

## Variables & types scalaires

```python
# Affectation dynamique
x = 1
PI = 3.14

n = 10                               # int
prix = 19.99                         # float
ok = True                            # bool
s = "texte"                          # str
v = None                             # NoneType (absence de valeur)
u = 5                                # union logique (dynamique)

```

## Types agrégés

```python
obj = {"nom": "A", "age": 30}         # dict
arr = [1, 2, 3]                      # list (mutable)
tup = ("a", 1)                       # tuple (immuable)
ens = {1, 2, 3}                      # set (éléments uniques)
from enum import Enum
class Couleur(Enum): ROUGE = 1       # enum
opt = None                           # optionnel / nullable
ID = int | str                       # type alias (Python 3.10+)

```

## Casting

```python
v1 = str(125)                        # int -> str ("125")
v2 = int("42")                       # str -> int (42)
v3 = float("19.99")                  # str -> float (19.99)
v4 = list({1, 2, 3})                 # set -> list

```

## Opérateurs

```python
+ - * / // % **                      # arithmétiques (// entière, ** puissance)
== != < > <= >=                      # relationnels
and or not                           # logiques
= += -= *=                           # affectation
x if condition else y                # ternaire
a | b                                # union d'ensembles ou de types

```

## Contrôle de flux

```python
if x > 0: pass
elif x == 0: pass
else: pass

match x:                             # Python 3.10+
    case 1: pass
    case _: pass

for i in range(10): pass
for item in arr: pass
for k, v in obj.items(): pass
while x < 10: pass

```

## Fonctions

```python
def add(a: int, b: int) -> int: return a + b
def sum_all(*nums: int) -> int: return sum(nums)
mul = lambda a, b: a * b             # anonyme / lambda
def identity(val: T) -> T: return val # générique

list(map(lambda x: x * 2, arr))
list(filter(lambda x: x > 0, arr))
from functools import reduce
reduce(lambda acc, x: acc + x, arr, 0)

```

## Exceptions

```python
try:
    raise ValueError("oups")
except ValueError as e:
    print(e)
finally:
    pass                             # toujours exécuté

```

## Modules & Packages

```python
# mon_module.py
def f(): pass
class C: pass
o = {}

# main.py
from mon_module import f, C, o
import os
from pathlib import Path

```

## Fichiers & Répertoires

```python
# Modes open(): 'r' (lecture), 'w' (écriture/écrasement), 'a' (ajout), 'b' (binaire)

# Lecture / Écriture de texte
with open("fichier.txt", "r", encoding="utf-8") as f:
    texte = f.read()                 # lit tout
    for line in f: pass              # itération ligne par ligne

with open("fichier.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")

# Accès aléatoire (binaire / texte)
with open("data.bin", "rb") as f:
    f.seek(10)                        # déplace le pointeur au 10ème octet
    pos = f.tell()                   # position actuelle du pointeur

# Répertoires & Chemins (pathlib)
from pathlib import Path

p = Path("dossier/sous_dossier/fichier.txt")
p.parent.mkdir(parents=True, exist_ok=True)  # mkdirs (crée parents)
p.exists()                           # vérifie si existe
p.is_file()                          # est un fichier
p.is_dir()                           # est un dossier
content = p.read_text(encoding="utf-8")      # lecture directe
p.write_text("ok", encoding="utf-8")         # écriture directe

```

## POO simple (Bases & Encapsulation)

```python
class CompteBancaire:
    def __init__(self, titulaire: str, solde: float = 0.0):
        self.titulaire = titulaire   # attribut public
        self._solde = solde          # attribut protégé (convention)
        self.__secret = "1234"       # attribut privé (name mangling)

    def deposer(self, montant: float):
        if montant > 0: self._solde += montant

    @property                        # getter
    def solde(self) -> float:
        return self._solde

    @solde.setter                    # setter avec contrôle
    def solde(self, valeur: float):
        if valeur >= 0: self._solde = valeur

    def __str__(self) -> str:        # méthode spéciale (dunder)
        return f"Compte({self.titulaire}, {self._solde}€)"

compte = CompteBancaire("Alice", 100)
compte.deposer(50)
print(compte.solde)                  # appel du getter (150)

```

## POO avancée (Héritage & Abstraction)

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    espece = "inconnue"               # attribut de classe / static
    def __init__(self, nom: str):
        self._nom = nom

    @abstractmethod
    def crier(self): pass

class Chien(Animal):
    def __init__(self, nom: str, race: str):
        super().__init__(nom)        # chaînage des constructeurs
        self.race = race

    def crier(self):                 # polymorphisme
        print(f"{self._nom} aboie")

class Generique[T]:
    def __init__(self, v: T):
        self.valeur = v

```

## Asynchrone

```python
import asyncio

async def attendre(ms: int):
    await asyncio.sleep(ms / 1000)

async def main():
    await attendre(1000)
    print("fait")

# asyncio.run(main())

```

## Tests (Pytest / Unittest)

```python
# test_main.py
def test_cas():
    assert 1 + 1 == 2

from unittest.mock import Mock
mock = Mock()

```
