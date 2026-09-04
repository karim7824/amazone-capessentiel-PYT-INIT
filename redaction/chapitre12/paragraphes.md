# Chapitre 12 : Un code plus robuste en prenant en compte les erreurs

La gestion des erreurs permet d'anticiper et de traiter les incidents d'exécution pour empêcher l'arrêt brutal d'un programme en Python. Maîtriser ces mécanismes est indispensable pour concevoir des applications fiables et résilientes.
Dans ce chapitre :

* Gestion des exceptions (`try`, `except`, `finally`) et levée d'exceptions (`raise`)


* Utilisation de l'instruction `finally`

* Émission personnalisée d'une exception



---

## Gestion des exceptions : try catch finally et throw

La gestion des exceptions repose sur le bloc `try` pour surveiller le code à risque et `except` pour intercepter les erreurs survenues. En Python, le mot-clé `raise` équivaut au `throw` des autres langages pour émettre une exception.

```python
# Interception d'une division par zéro
try:
    resultat = 10 / 0
except ZeroDivisionError:
    resultat = "Erreur : Division par zéro impossible"

```

> 💡 Spécifiez toujours le type précis d'exception à intercepter dans votre bloc `except` plutôt que d'utiliser une clause globale muette qui masquerait des bugs inattendus.

---

## Instruction finally

L'instruction `finally` permet de définir un bloc de code qui s'exécute systématiquement à la fin, qu'une exception ait été levée ou non. Elle est idéale pour libérer des ressources (fichiers, connexions réseau).

```python
# Utilisation de finally pour la clôture des ressources
try:
    fichier = ouvrir_fichier("donnees.txt")
except FileNotFoundError:
    print("Fichier introuvable")
finally:
    fermer_fichier()  # Exécuté dans tous les cas

```

> 💡 Privilégiez l'utilisation du gestionnaire de contexte `with` lorsque c'est possible pour automatiser le nettoyage des ressources sans recourir explicitement à un bloc `finally`.

---

## Emettre une exception avec throw

Il est possible d'émettre volontairement une exception à l'aide de l'instruction `raise` (similaire à `throw`) pour signaler qu'une règle métier ou une condition critique n'est pas respectée.

```python
# Émission d'une exception si l'âge est invalide
age = -5
if age < 0:
    raise ValueError("L'âge ne peut pas être négatif")

```

> 💡 Créez vos propres classes d'exceptions personnalisées en héritant de la classe `Exception` de base pour affiner la gestion des erreurs spécifiques à votre domaine métier.

---

## Exemple de synthèse

```python
# Programme complet combinant try, except, finally et la levée d'une exception avec raise

def convertir_et_diviser(valeur_str, diviseur_str):
    """Convertit deux chaînes en entiers et réalise une division sécurisée."""
    try:
        valeur = int(valeur_str)
        diviseur = int(diviseur_str)
        
        # Émission d'une exception personnalisée si le diviseur est nul
        if diviseur == 0:
            raise ZeroDivisionError("Le diviseur ne peut pas être égal à zéro.")
            
        quotient = valeur / diviseur
    except ValueError as e:
        return f"Erreur de format numérique : {e}"
    except ZeroDivisionError as e:
        return f"Erreur mathématique : {e}"
    finally:
        print("Fin de l'opération de calcul sécurisée.")
        
    return f"Résultat du calcul : {quotient}"

# Test de la fonction avec des valeurs littérales
print(convertir_et_diviser("100", "4"))
print(convertir_et_diviser("50", "0"))

```

### Exercices de fin de chapitre

1. **Exercice 1 :** Écrivez un script qui demande à l'utilisateur de saisir un nombre, utilise un bloc `try...except` pour intercepter une éventuelle erreur de saisie (`ValueError`), et affiche un message adapté.
2. **Exercice 2 :** Créez une fonction qui vérifie si un mot de passe possède au moins 8 caractères. Si ce n'est pas le cas, utilisez `raise` pour émettre une exception personnalisée de type `ValueError`.
