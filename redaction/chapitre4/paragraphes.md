# Chapitre 4 : Manipulation des chaines de caractères

La manipulation des chaînes de caractères permet de traiter, formetter et analyser des données textuelles en Python. Maîtriser ces outils est indispensable pour interagir avec les utilisateurs et structurer des messages lisibles.
Dans ce chapitre :

* Gestion des chaines
* Formatage
* Slicing
* Expressions régulières

---

## Gestion des chaines

La gestion des chaînes de caractères repose sur l'utilisation de guillemets simples ou doubles pour déclarer du texte en mémoire. Python fournit de nombreuses méthodes intégrées pour transformer, nettoyer ou rechercher des motifs textuels.

```python
# Manipulation de base d'une chaîne de caractères
texte = "  formation python  "
texte_propre = texte.strip().capitalize()

```

> 💡 Les chaînes de caractères en Python sont immuables : toute modification textuelle génère un nouvel objet en mémoire plutôt que de modifier la chaîne originale.

---

## Formatage

Le formatage permet d'insérer dynamiquement des variables ou des expressions au sein d'une chaîne de caractères de manière lisible et performante. Les f-strings constituent la méthode moderne recommandée en Python.

```python
# Utilisation des f-strings pour l'interpolation de variables
langage = "Python"
version = 3.10
message = f"Apprentissage de {langage} en version {version}"

```

> 💡 Préférez toujours l'utilisation des f-strings par rapport aux anciennes méthodes de formatage (`%` ou `.format()`) pour gagner en lisibilité et en performance.

---

## Slicing

Le slicing (ou découpage) permet d'extraire une portion spécifique d'une chaîne de caractères en spécifiant des indices de début, de fin et de pas.

```python
# Extraction d'une sous-chaîne par découpage
code_complet = "PYTH-2026"
prefixe = code_complet[:4]  # Extrait "PYTH"

```

> 💡 En Python, les indices de découpage commencent à zéro et l'indice de fin spécifié est toujours exclus du résultat extrait.

---

## Expressions régulières

Les expressions régulières permettent de rechercher, valider ou extraire des motifs complexes dans des chaînes de caractères en s'appuyant sur le module standard `re`.

```python
import re

# Validation d'un format de code postal à 5 chiffres
code_postal = "75001"
est_valide = bool(re.match(r"^\d{5}$", code_postal))

```

> 💡 Testez toujours vos expressions régulières sur des cas limites avant de les intégrer en production pour éviter des comportements inattendus sur les données textuelles.

---

## Exemple de synthèse

```python
import re

# Programme complet combinant gestion, formatage, slicing et expressions régulières
reference_brute = "   REF-9876-FR   "

# 1. Gestion : nettoyage des espaces superflus et mise en majuscules
reference_nette = reference_brute.strip()

# 2. Slicing : extraction de la portion numérique centrale
code_numerique = reference_nette[4:8]

# 3. Expressions régulières : validation du format global
pattern = r"^REF-\d{4}-[A-Z]{2}$"
est_conforme = bool(re.match(pattern, reference_nette))

# 4. Formatage : construction du message final avec une f-string
rapport = f"Référence : {reference_nette} | Code extrait : {code_numerique} | Conforme : {est_conforme}"
print(rapport)

```

## Exercices

1. **Exercice 1 :** Écrivez un script qui prend une chaîne de caractères contenant des espaces superflus et du texte en minuscules, puis utilisez les méthodes de gestion pour la nettoyer et la mettre entièrement en majuscules.
2. **Exercice 2 :** Déclarez une chaîne contenant un numéro de téléphone sous la forme d'une phrase, puis utilisez le slicing pour extraire les deux premiers caractères et formotez un message personnalisé à l'aide d'une f-string.