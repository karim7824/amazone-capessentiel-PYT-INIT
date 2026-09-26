# Chapitre 12 : Un code plus robuste en prenant en compte les erreurs

La gestion des erreurs permet d'anticiper et de traiter les incidents d'exécution pour empêcher l'arrêt brutal d'un programme en Python. Maîtriser ces mécanismes est indispensable pour concevoir des applications fiables et résilientes.
Dans ce chapitre :

* Gestion des exceptions (`try`, `except`, `finally`) et levée d'exceptions (`raise`)
* Utilisation de l'instruction `finally`
* Émission personnalisée d'une exception

---

## Gestion des exceptions : try catch finally et throw

La gestion des exceptions repose sur le bloc `try` pour surveiller le code à risque et `except` pour intercepter les erreurs survenues. En Python, le mot-clé `raise` équivaut au `throw` des autres langages pour émettre une exception. On peut intercepter une exception précise ZeroDivisionError pour la traiter ou intercepter toutes les exceptions dans un même traitement

```python
# Interception d'une division par zéro
try:
    resultat = 10 / 0
    i+=1  # incrémenter une variable i qui n'existe pas 
except ZeroDivisionError:
    print("Erreur : Division par zéro impossible")
except Exception as e:
    print("Problème ", e)

# Plus de division par zéro mais "Problème  name 'i' is not defined"
try:
    resultat = 10 / 0
    i+=1  # incrémenter une variable i qui n'existe pas 
except ZeroDivisionError:
    print("Erreur : Division par zéro impossible")
except Exception as e:
    print("Problème ", e)

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
def traitement (eleve):
    if eleve['age'] < 0:
        #raise ValueError("L'âge ne peut pas être négatif") # ValueError: L'âge ne peut pas être négatif
        raise Exception ("L'âge ne peut pas être négatif")  # Exception: L'âge ne peut pas être négatif
    print(f"{eleve['nom']} -- {eleve['age']} ")

eleve = { 'nom' : 'karim', 'age' : 20}
traitement (eleve) # OK
eleve = { 'nom' : 'karim', 'age' : -20}
traitement (eleve) # exception prooduite qu'il faut intercepter dans un bloc try/except

```

> 💡 Créez vos propres classes d'exceptions personnalisées en héritant de la classe `Exception` de base pour affiner la gestion des erreurs spécifiques à votre domaine métier.
---
## Trace et log
Si la gestion des exceptions permet à un programme de réagir aux erreurs au moment où elles se produisent, **les traces et les logs** sont indispensables pour comprendre ce qui s'est passé en coulisses, analyser le comportement de l'application au fil du temps et déboguer plus facilement.

* **Les logs (journalisation) :** Un log est un enregistrement horodaté d'un événement précis survenu lors de l'exécution.Ils sont catégorisés par niveau de gravité (`INFO`, `WARNING`, `ERROR`, `CRITICAL`) pour filtrer les informations selon les besoins.Les logs permettent de garder un historique de la vie du système, notamment en environnement de production où l'affichage direct à l'écran n'est pas possible.
* **Les traces (ou *stack traces*) :** Lorsqu'une exception est levée (via `throw`) et non interceptée immédiatement, le langage génère une **trace d'exécution**. Cette trace agit comme un fil d'Ariane : elle liste la suite d'appels de fonctions, les fichiers et les numéros de lignes traversés jusqu'au point exact de la défaillance.

En pratique, la combinaison des deux est essentielle pour la robustesse : lors de la capture d'une exception dans un bloc `try/catch`, enregistrer la **trace** complète au sein d'un **log** de niveau `ERROR` permet aux développeurs de reconstituer précisément le contexte de la panne sans interrompre le service pour les autres utilisateurs.

Le niveau logger.exception() enregistre le message en niveau ERROR et inclut automatiquement la stack trace complète.

Python
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    resultat = 10 / 0
except ZeroDivisionError:
    logger.exception("Une erreur de division par zéro est survenue")
```
Si tu souhaites utiliser un autre niveau de log (par exemple `CRITICAL` ou `WARNING`), ajoute le paramètre `exc_info=True`.

```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    logger.warning("Attention, calcul impossible !", exc_info=True)

```
Si tu as besoin de manipuler ou de mettre en forme la stack trace avant de la logger (ou sans lever d'exception), utilise le module standard `traceback`.

```python
import logging
import traceback

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    resultat = 10 / 0
except ZeroDivisionError:
    # Convertit la stack trace en str
    trace_str = traceback.format_exc()
    logger.error(f"Détail de l'erreur :\n{trace_str}")

```
Si tu souhaites afficher la chaîne d'appels courante dans les logs pour du débogage, sans qu'il n'y ait d'erreur :

```python
import logging
import traceback

def ma_fonction():
    # Capture la pile d'exécution actuelle
    stack = "".join(traceback.format_stack())
    logger.debug(f"Pile d'appel actuelle :\n{stack}")

ma_fonction()

```

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

## Exercices de fin de chapitre

**Exercice 1 :** Écrivez un script qui demande à l'utilisateur de saisir un nombre, utilise un bloc `try...except` pour intercepter une éventuelle erreur de saisie (`ValueError`), et affiche un message adapté.

**Exercice 2 :** Créez une fonction qui vérifie si un mot de passe possède au moins 8 caractères. Si ce n'est pas le cas, utilisez `raise` pour émettre une exception personnalisée de type `ValueError`.
