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
python -m pytest                     # exécuter les tests unitaire
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

## Programmation orientée objet

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    espece = "inconnue"               # attribut de classe / static
    def __init__(self, nom: str):
        self._nom = nom              # protégé
    @abstractmethod
    def crier(self): pass

class Chien(Animal):
    def crier(self):
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