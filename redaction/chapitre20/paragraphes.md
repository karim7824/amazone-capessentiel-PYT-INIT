# Solutions des exercices Python

---

**Chapitre 1 / Exercice 1 **

Voici l'instruction en Python pour afficher la version exacte de l'interpréteur :

```python
import sys

print(sys.version)

```

Le module standard `os` permet d'accéder aux variables d'environnement via le dictionnaire `os.environ`.

```python
import os

#Récupération sécurisée de la variable PATH
path_env = os.environ.get("PATH", "Variable non trouvée")
print(path_env)

```

Le module standard `subprocess` est l'outil officiel et sécurisé pour exécuter des commandes système.

```python
import subprocess

#Exécution de la commande shell 'dir' (sur Windows) ou 'ls' (sur Linux/macOS)
résultat = subprocess.run("dir", shell=True, text=True, capture_output=True)

# Affichage de la sortie standard
print(résultat.stdout)

```

> 💡 **Bonne pratique :** Privilégiez `subprocess.run()` avec `shell=True` si vous devez récupérer le texte généré par la commande ou gérer d'éventuelles erreurs.

**Chapitre 1 / Exercice 2 **

```python
# La fonction range(1, 11) produit les entiers de 1 à 10
for i in range(1, 11):
    print("O" * i)
```

**Chapitre 2 / Exercice 1 
```python
from pathlib import Path

def saluer(nom: str) -> str:
    """Génère un message de salutation à partir d'un nom."""
    return f"Bonjour {nom}, bienvenue !"

if __name__ == '__main__':
    # Définition du prénom
    prenom = "Karim"
    
    # Génération du message
    message = saluer(prenom)
    
    # Écriture du message dans le fichier bienvenue.txt avec pathlib
    fichier = Path("bienvenue.txt")
    fichier.write_text(message, encoding="utf-8")
    
    # Confirmation dans la console
    print(f"Message écrit dans '{fichier.name}' : {message}")

```

**Chapitre 2 / Exercice 2
```python
import sys
from pathlib import Path

def est_dans_venv() -> bool:
    """Vérifie si le script est exécuté dans un environnement virtuel (venv)."""
    # sys.prefix != sys.base_prefix indique qu'un environnement virtuel est actif
    return sys.prefix != sys.base_prefix

def verifier_environnement() -> None:
    """Contrôle l'environnement et consigne le statut."""
    log_file = Path("env_status.log")

    if est_dans_venv():
        # Récupération du chemin de l'interpréteur actuel
        executable_path = sys.executable
        log_content = f"Environnement virtuel actif.\nInterpréteur : {executable_path}\n"
        
        # Écriture dans le fichier journal
        log_file.write_text(log_content, encoding="utf-8")
        print(f"[OK] Environnement virtuel détecté. Détails écrits dans {log_file.name}")
    else:
        print("[AVERTISSEMENT] Vous n'êtes pas dans un environnement virtuel !")
        print("Il est fortement recommandé d'en activer un (ex: 'source venv/bin/activate' ou 'venv\\Scripts\\activate').")

if __name__ == "__main__":
    verifier_environnement()
	
```	
**Chapitre 3 / Exercice 1 
```python
def afficher_types() -> None:
    """Déclare quatre variables scalaires et affiche leur type."""
    # Déclaration des quatre variables de types scalaires
    nombre_entier: int = 42
    nombre_decimal: float = 3.14
    est_actif: bool = True
    chaine_texte: str = "Python"

    # Affichage de la valeur et du type de chaque variable
    print(f"Valeur : {nombre_entier:<10} | Type : {type(nombre_entier)}")
    print(f"Valeur : {nombre_decimal:<10} | Type : {type(nombre_decimal)}")
    print(f"Valeur : {str(est_actif):<10} | Type : {type(est_actif)}")
    print(f"Valeur : {chaine_texte:<10} | Type : {type(chaine_texte)}")


if __name__ == "__main__":
    afficher_types()
```	

**Chapitre 3 / Exercice 2
```python
def calculer_moyenne(notes: list[float]) -> float:
    """Calcule la moyenne d'une liste de notes numériques."""
    if not notes:
        return 0.0

    # Somme des notes divisée par le nombre d'éléments
    total = sum(notes)
    nombre_de_notes = len(notes)
    
    # Stockage dans une variable locale
    moyenne_calculee = total / nombre_de_notes
    
    return moyenne_calculee


if __name__ == "__main__":
    # Liste des notes de l'étudiant
    notes_etudiant = [14.5, 12.0, 16.5, 9.0, 15.0]

    # Appel de la fonction et affichage du résultat
    moyenne_finale = calculer_moyenne(notes_etudiant)
    print(f"Notes de l'étudiant : {notes_etudiant}")
    print(f"Moyenne calculée   : {moyenne_finale:.2f} / 20")```	

**Chapitre 4 / Exercice 1 
```python
def calculer_operations(a: int, b: int) -> None:
    """Calcule et affiche la somme, le produit et le reste de la division entière de deux nombres."""
    somme = a + b
    produit = a * b
    
    # Gestion du cas de la division par zéro
    reste = a % b if b != 0 else None

    print(f"Nombre A : {a}")
    print(f"Nombre B : {b}")
    print(f"Somme (a + b)                : {somme}")
    print(f"Produit (a * b)              : {produit}")
    if reste is not None:
        print(f"Reste de la division (a % b) : {reste}")
    else:
        print("Reste de la division (a % b) : Impossible (division par zéro)")


if __name__ == "__main__":
    # Initialisation des deux variables numériques
    nombre_1 = 25
    nombre_2 = 4

    calculer_operations(nombre_1, nombre_2)
```	
**Chapitre 4 / Exercice 2
```python
def verifier_acces(age: int, a_autorisation: bool) -> bool:
    """Vérifie si l'utilisateur remplit les conditions d'accès."""
    # Condition : être majeur (>= 18) ET posséder une autorisation
    est_autorise = (age >= 18) and a_autorisation
    return est_autorise


if __name__ == "__main__":
    # Déclaration des variables de test
    age_utilisateur = 20
    a_autorisation = True

    # Vérification des conditions
    acces_accorde = verifier_acces(age_utilisateur, a_autorisation)

    print(f"Âge de l'utilisateur : {age_utilisateur} ans")
    print(f"Possède une autorisation : {a_autorisation}")
    
    if acces_accorde:
        print("Résultat : Accès ACCORDÉ")
    else:
        print("Résultat : Accès REFUSÉ")
```	

**Chapitre 5 / Exercice 1 
```python
def calculer_prix_ttc(prix_ht_str: str) -> int:
    """Convertit un prix HT sous forme de chaîne, applique la TVA de 20% 
    et renvoie le montant TTC arrondi sous forme d'entier.
    """
    # Conversion de la chaîne en float
    prix_ht = float(prix_ht_str)
    
    # Application de la taxe de 20%
    prix_ttc_float = prix_ht * 1.20
    
    # Conversion du résultat final en int (troncature / arrondi)
    prix_ttc_int = int(prix_ttc_float)
    
    return prix_ttc_int


if __name__ == "__main__":
    # Chaîne initiale représentant le prix avec décimales
    prix_chaine = "49.99"
    
    # Exécution du calcul
    resultat = calculer_prix_ttc(prix_chaine)
    
    print(f"Prix HT initial (str)   : '{prix_chaine}'")
    print(f"Prix TTC converti (int) : {resultat} €")
```	

**Chapitre 5 / Exercice 2
```python
def observer_conversion_implicite() -> None:
    """Effectue l'addition d'un entier et d'un flottant pour observer le type du résultat."""
    # Déclaration d'un entier (int) et d'un flottant (float)
    nombre_entier: int = 15
    nombre_flottant: float = 4.5

    # Addition des deux variables (conversion implicite par Python)
    resultat = nombre_entier + nombre_flottant

    # Affichage des valeurs et de leurs types
    print(f"Valeur 1 (entier)   : {nombre_entier} | Type : {type(nombre_entier)}")
    print(f"Valeur 2 (flottant) : {nombre_flottant} | Type : {type(nombre_flottant)}")
    print(f"Résultat            : {resultat} | Type : {type(resultat)}")


if __name__ == "__main__":
    observer_conversion_implicite()
```	

**Chapitre 6 / Exercice 1 
```python
def nettoyer_et_capitaliser(texte_brut: str) -> str:
    """Supprime les espaces superflus en début/fin de chaîne 

    et convertit le texte intégralement en majuscules.
    """
    # 1. Suppression des espaces superflus aux extrémités avec strip()
    texte_epure = texte_brut.strip()
    
    # 2. Conversion en majuscules avec upper()
    texte_majuscule = texte_epure.upper()
    
    return texte_majuscule


if __name__ == "__main__":
    # Chaîne initiale avec espaces inutiles et minuscules
    chaine_initiale = "   bienvenue dans le cours de python !   "

    # Application des méthodes de nettoyage
    chaine_nettoyee = nettoyer_et_capitaliser(chaine_initiale)

    print(f"Chaîne initiale : '{chaine_initiale}'")
    print(f"Chaîne nettoyée : '{chaine_nettoyee}'")
```	
**Chapitre 6 / Exercice 2
```python
def extraire_et_formater(phrase: str, nom_utilisateur: str) -> str:
    """Extrait l'indicatif régional d'un numéro présent dans une phrase

    et génère un message personnalisé à l'aide d'une f-string.
    """
    # Slicing des 2 premiers caractères ([début:fin])
    indicatif = phrase[:2]

    # Formatage du message personnalisé avec une f-string
    message_formate = f"Bonjour {nom_utilisateur}, votre indicatif régional est le +{indicatif}."

    return message_formate


if __name__ == "__main__":
    # Chaîne initiale avec le numéro au début de la phrase
    phrase_telephone = "33 6 12 34 56 78 est le numéro de contact."
    prenom = "Karim"

    # Extraction et génération du message
    resultat = extraire_et_formater(phrase_telephone, prenom)

    print(f"Phrase source : '{phrase_telephone}'")
    print(f"Message généré : {resultat}")
```	

**Chapitre 7 / Exercice 1 
```python
import random

def analyser_parite_liste(taille: int = 10) -> tuple[int, int]:
    """Génère une liste de nombres aléatoires et compte les éléments pairs et impairs."""
    # Génération d'une liste de 10 valeurs aléatoires entre 0 et 99 inclus
    valeurs: list[int] = [random.randrange(100) for _ in range(taille)]
    
    compteur_pairs: int = 0
    compteur_impairs: int = 0

    # Parcours du tableau
    for nombre in valeurs:
        if nombre % 2 == 0:
            compteur_pairs += 1
        else:
            compteur_impairs += 1

    # Affichage des détails
    print(f"Liste générée : {valeurs}")
    print(f"Nombres pairs   : {compteur_pairs}")
    print(f"Nombres impairs : {compteur_impairs}")

    return compteur_pairs, compteur_impairs


if __name__ == "__main__":
    analyser_parite_liste()
```	

**Chapitre 7 / Exercice 2
```python
def assembler_noms_et_ages(noms: list[str], ages: list[int]) -> dict[str, int]:
    """Assemble deux listes (noms et âges) pour former un dictionnaire nom: âge."""
    # Dictionnaire résultat
    annuaire: dict[str, int] = {}

    # Option 1 : Assemblage avec une boucle basée sur les indices
    for i in range(len(noms)):
        cle = noms[i]
        valeur = ages[i]
        annuaire[cle] = valeur

    return annuaire


if __name__ == "__main__":
    # Déclaration des deux listes
    liste_noms = ["toto1", "toto2", "toto3", "toto4"]
    liste_ages = [20, 25, 30, 35]

    # Appel de la fonction
    resultat = assembler_noms_et_ages(liste_noms, liste_ages)

    print(f"Liste des noms : {liste_noms}")
    print(f"Liste des âges : {liste_ages}")
    print(f"Dictionnaire  : {resultat}")
```	

**Chapitre 7 / Exercice 3
```python
import random

def separer_parite(taille: int = 10) -> tuple[list[int], list[int]]:
    """Génère une liste d'entiers aléatoires et la sépare en deux listes : 

    l'une contenant les nombres pairs, l'autre les nombres impairs.
    """
    # Génération d'un tableau de 10 valeurs aléatoires entre 0 et 99
    valeurs: list[int] = [random.randrange(100) for _ in range(taille)]
    
    # Initialisation des deux listes réceptrices
    pairs: list[int] = []
    impairs: list[int] = []

    # Parcours du tableau initial
    for nombre in valeurs:
        if nombre % 2 == 0:
            pairs.append(nombre)
        else:
            impairs.append(nombre)

    # Affichage des résultats
    print(f"Tableau initial : {valeurs}")
    print(f"Tableau pairs   : {pairs}")
    print(f"Tableau impairs : {impairs}")

    return pairs, impairs


if __name__ == "__main__":
    separer_parite()
```	

**Chapitre 8 / Exercice 1 
```python
def traiter_liste_imbriquee(nombre_elements: int = 5) -> list[list[object]]:
    """Génère une liste de sous-listes [nom, entier] 

    puis parcourt la structure pour afficher uniquement les noms.
    """
    liste_principale: list[list[object]] = []

    # 1. Génération de la liste de sous-listes via une boucle
    for i in range(1, nombre_elements + 1):
        nom = f"TOTO{i}"
        sous_liste = [nom, i]
        liste_principale.append(sous_liste)

    print(f"Liste générée : {liste_principale}\n")
    print("Affichage des noms uniquement :")

    # 2. Parcours de la liste imbriquée et extraction du premier élément
    for sous_liste in liste_principale:
        nom = sous_liste[0]  # Récupération de l'élément à l'index 0 ('TOTOx')
        print(nom)

    return liste_principale


if __name__ == "__main__":
    traiter_liste_imbriquee()
```	
**Chapitre 8 / Exercice 2
```python
def traiter_liste_dictionnaires(nombre_elements: int = 5) -> list[dict[str, object]]:
    """Génère une liste de dictionnaires {'nom': str, 'age': int}

    puis parcourt la structure pour afficher uniquement les noms.
    """
    liste_personnes: list[dict[str, object]] = []

    # 1. Génération de la liste de dictionnaires via une boucle
    for i in range(1, nombre_elements + 1):
        personne = {
            "nom": f"TOTO{i}",
            "age": i
        }
        liste_personnes.append(personne)

    print(f"Liste générée : {liste_personnes}\n")
    print("Affichage des noms uniquement :")

    # 2. Parcours de la liste et extraction de la valeur associée à la clé 'nom'
    for personne in liste_personnes:
        nom = personne["nom"]
        print(nom)

    return liste_personnes


if __name__ == "__main__":
    traiter_liste_dictionnaires()
```	

**Chapitre 8 / Exercice 3
```python
def filtrer_fruits_par_prix(catalogue: dict[str, float], prix_seuil: float) -> None:
    """Parcourt le dictionnaire de fruits et affiche ceux dont le prix dépasse le seuil fixé."""
    print(f"Catalogue des fruits coûtant strictement plus de {prix_seuil:.2f} € :\n")

    # Parcours simultané des clés (fruits) et des valeurs (prix) via .items()
    for fruit, prix in catalogue.items():
        if prix > prix_seuil:
            print(f"- {fruit.capitalize():<10} : {prix:.2f} €")


if __name__ == "__main__":
    # Dictionnaire associant chaque fruit à son prix unitaire en euros
    prix_fruits: dict[str, float] = {
        "pomme": 1.50,
        "ananas": 3.80,
        "banane": 0.90,
        "mangue": 2.50,
        "orange": 1.20,
        "fraise": 4.20
    }

    seuil_defaut = 2.00
    filtrer_fruits_par_prix(prix_fruits, seuil_defaut)
```	

**Chapitre 9 / Exercice 1 
```python
def calculer_moyenne_args(*nombres: int) -> float:
    """Calcule la moyenne arithmétique d'un nombre indéfini d'entiers."""
    # *nombres est un tuple contenant tous les arguments transmis
    if not nombres:
        return 0.0

    total = sum(nombres)
    quantite = len(nombres)

    return total / quantite


if __name__ == "__main__":
    # Exemples d'appels avec un nombre variable d'arguments
    moyenne_1 = calculer_moyenne_args(10, 12, 14, 16)
    moyenne_2 = calculer_moyenne_args(5, 15, 20)
    moyenne_vide = calculer_moyenne_args()

    print(f"Moyenne (10, 12, 14, 16) : {moyenne_1:.2f}")
    print(f"Moyenne (5, 15, 20)      : {moyenne_2:.2f}")
    print(f"Moyenne (aucun argument) : {moyenne_vide:.2f}")
```	

**Chapitre 9 / Exercice 2
```python
from typing import Callable

def appliquer_operation(
    fonction_math: Callable[[float, float], float], 
    a: float, 
    b: float
) -> float:
    """Applique la fonction mathématique passée en paramètre aux deux nombres a et b."""
    return fonction_math(a, b)


# Exemples de fonctions à passer en paramètre
def additionner(x: float, y: float) -> float:
    return x + y

def multiplier(x: float, y: float) -> float:
    return x * y


if __name__ == "__main__":
    nombre_1 = 12.0
    nombre_2 = 4.0

    # Passage de fonctions nommées en argument
    res_addition = appliquer_operation(additionner, nombre_1, nombre_2)
    res_multiplication = appliquer_operation(multiplier, nombre_1, nombre_2)

    # Passage d'une fonction anonyme (lambda)
    res_puissance = appliquer_operation(lambda x, y: x ** y, nombre_1, nombre_2)

    print(f"Addition ({nombre_1} + {nombre_2})        : {res_addition}")
    print(f"Multiplication ({nombre_1} * {nombre_2})  : {res_multiplication}")
    print(f"Puissance ({nombre_1} ^ {nombre_2})       : {res_puissance}")
```	

**Chapitre 10 / Exercice 1 
```python
def filtrer_mots_longs(mots: list[str], longueur_min: int = 5) -> list[str]:
    """Extrait d'une liste les mots ayant une longueur strictement supérieure à longueur_min."""
    # Utilisation de filter() avec une expression lambda
    iterateur_mots_longs = filter(lambda mot: len(mot) > longueur_min, mots)
    
    # Conversion de l'itérateur filter en liste
    return list(iterateur_mots_longs)


if __name__ == "__main__":
    # Liste initiale de mots
    liste_mots = ["arbre", "soleil", "ordinateur", "clef", "python", "code", "développement"]

    # Exécution du filtrage
    mots_filtres = filtrer_mots_longs(liste_mots, 5)

    print(f"Liste d'origine : {liste_mots}")
    print(f"Mots de plus de 5 caractères : {mots_filtres}")
```	
**Chapitre 10 / Exercice 2
```python
from functools import reduce

def calculer_produit_liste(nombres: list[int]) -> int:
    """Calcule le produit cumulé de tous les entiers d'une liste via reduce()."""
    if not nombres:
        return 0

    # reduce() applique la fonction lambda cumulée sur la liste
    produit_total = reduce(lambda acc, val: acc * val, nombres)
    
    return produit_total


if __name__ == "__main__":
    # Liste initiale d'entiers
    liste_nombres = [2, 3, 4, 5]

    # Calcul du produit
    resultat = calculer_produit_liste(liste_nombres)

    print(f"Liste d'entiers : {liste_nombres}")
    print(f"Produit total    : {resultat}")
```	

**Chapitre 11 / Exercice 1 
```python
from typing import Generator

def generer_nombres_pairs(limite: int) -> Generator[int, None, None]:
    """Générateur produisant les nombres pairs de 0 jusqu'à la limite incluse."""
    actuel = 0
    while actuel <= limite:
        yield actuel
        actuel += 2


if __name__ == "__main__":
    limite_maximale = 10

    print(f"Séquence des nombres pairs jusqu'à {limite_maximale} :")
    
    # Parcours du générateur à l'aide d'une boucle for
    for nombre in generer_nombres_pairs(limite_maximale):
        print(nombre, end=" ")
    print()  # Saut de ligne final
```	
**Chapitre 11 / Exercice 2
```python
from typing import Iterator

def consommer_expression_generatrice() -> None:
    """Instancie une expression génératrice pour les carrés de 1 à 10

    et extrait chaque valeur séquentiellement avec next().
    """
    # Expression génératrice entourée de parenthèses (évaluation paresseuse)
    carres_gen: Iterator[int] = (x ** 2 for x in range(1, 11))

    print("Extraction manuelle des valeurs avec next() :\n")

    # Récupération de la première valeur
    premier = next(carres_gen)
    print(f"Premier élément  : {premier}")

    # Récupération de la deuxième valeur
    deuxieme = next(carres_gen)
    print(f"Deuxième élément : {deuxieme}")

    # Récupération de la troisième valeur
    troisieme = next(carres_gen)
    print(f"Troisième élément: {troisieme}")

    # Parcoure le reste des valeurs générées
    print("\nParcours du reste du générateur :")
    for valeur in carres_gen:
        print(valeur, end=" ")
    print()


if __name__ == "__main__":
    consommer_expression_generatrice()
```	

**Chapitre 12 / Exercice 1 
```python
def demander_nombre_entier() -> int:
    """Demande un nombre entier à l'utilisateur et gère l'exception ValueError

    en cas de saisie invalide.
    """
    saisie = input("Veuillez saisir un nombre entier : ")

    try:
        # Tentative de conversion de la chaîne en entier
        nombre = int(saisie)
        print(f"Conversion réussie : vous avez saisi le nombre {nombre}.")
        return nombre

    except ValueError:
        # Interception de l'erreur si la saisie n'est pas un nombre valide
        print(f"Erreur de saisie : '{saisie}' n'est pas un nombre entier valide.")
        return 0


if __name__ == "__main__":
    demander_nombre_entier()
```	

**Chapitre 12 / Exercice 2
```python
def valider_mot_de_passe(mot_de_passe: str) -> bool:
    """Vérifie la longueur minimale d'un mot de passe.

    Lève une exception ValueError si la longueur est inférieure à 8 caractères.
    """
    longueur_minimale = 8

    # Vérification de la contrainte de longueur
    if len(mot_de_passe) < longueur_minimale:
        raise ValueError(
            f"Mot de passe trop court ({len(mot_de_passe)} caractères). "
            f"Il doit contenir au moins {longueur_minimale} caractères."
        )

    print("Mot de passe valide.")
    return True


if __name__ == "__main__":
    # Test avec un mot de passe trop court
    mots_de_passe_test = ["pass123", "Securite2026!"]

    for mdp in mots_de_passe_test:
        print(f"\nTest du mot de passe : '{mdp}'")
        try:
            valider_mot_de_passe(mdp)
        except ValueError as erreur:
            print(f"Exception capturée : {erreur}")
```	

**Chapitre 13 / Exercice 1 
```python
def afficher_bienvenue(nom_utilisateur: str) -> None:
    """Affiche un message de bienvenue personnalisé."""
    print(f"Bienvenue, {nom_utilisateur} ! Le script s'exécute correctement.")


if __name__ == "__main__":
    # Ce bloc ne s'exécute que si le fichier est lancé directement
    print("Exécution du script en tant que programme principal.")
    
    nom = "Karim"
    afficher_bienvenue(nom)
```	
**Chapitre 13 / Exercice 2
```python
import sys

def saluer_utilisateur() -> None:
    """Récupère le nom passé en argument de ligne de commande via sys.argv

    et affiche une salutation personnalisée.
    """
    # sys.argv[0] contient toujours le nom du script lui-même.
    # On vérifie si un argument supplémentaire a été transmis.
    if len(sys.argv) < 2:
        print("Erreur : Aucun nom n'a été fourni en argument.")
        print(f"Usage : python {sys.argv[0]} <votre_nom>")
        sys.exit(1)

    # Extraction du premier argument après le nom du script
    nom_utilisateur: str = sys.argv[1]
    print(f"Bonjour {nom_utilisateur}, ravi de vous rencontrer !")


if __name__ == "__main__":
    saluer_utilisateur()
```	

**Chapitre 14 / Exercice 1 
```python
from pathlib import Path

def exporter_notes() -> None:
    """Crée un dossier 'export', y écris un fichier 'notes.txt' avec 3 lignes

    et affiche la taille du fichier en octets.
    """
    # Définition des chemins avec pathlib
    dossier_export = Path("export")
    fichier_notes = dossier_export / "notes.txt"

    # 1. Création du dossier 'export' s'il n'existe pas
    dossier_export.mkdir(parents=True, exist_ok=True)

    # Contenu de 3 lignes à écrire dans le fichier
    lignes = [
        "Première ligne : Introduction à la gestion des fichiers en Python.\n",
        "Deuxième ligne : Utilisation orientée objet de pathlib.Path.\n",
        "Troisième ligne : Export et calcul de métadonnées terminé.\n"
    ]

    # 2. Écriture du fichier texte avec encodage UTF-8
    with open(fichier_notes, mode="w", encoding="utf-8") as fichier:
        fichier.writelines(lignes)

    print(f"Fichier créé avec succès : {fichier_notes.resolve()}")

    # 3. Récupération et affichage de la taille du fichier
    taille_octets = fichier_notes.stat().st_size
    print(f"Taille du fichier : {taille_octets} octets")


if __name__ == "__main__":
    exporter_notes()
```	
**Chapitre 14 / Exercice 2
```python
import zipfile
from pathlib import Path

def archiver_fichiers_python(dossier_source: str | Path, nom_archive: str = "modules.zip") -> Path | None:
    """Recherche tous les fichiers .py dans le dossier_source (sans sous-dossiers)

    et les regroupe dans une archive ZIP nommée nom_archive.
    """
    chemin_dossier = Path(dossier_source)
    chemin_archive = chemin_dossier / nom_archive

    # Vérification de l'existence du dossier source
    if not chemin_dossier.is_dir():
        print(f"Erreur : Le dossier '{chemin_dossier}' n'existe pas ou n'est pas un répertoire.")
        return None

    # Recherche de tous les fichiers .py présents à la racine du dossier
    fichiers_py = list(chemin_dossier.glob("*.py"))

    if not fichiers_py:
        print(f"Aucun fichier .py trouvé dans {chemin_dossier}.")
        return None

    print(f"Fichiers Python trouvés ({len(fichiers_py)}) :")
    for f in fichiers_py:
        print(f" - {f.name}")

    # Création et écriture dans l'archive ZIP
    with zipfile.ZipFile(chemin_archive, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for fichier in fichiers_py:
            # arcname garantit d'inclure uniquement le nom du fichier dans l'archive (sans l'arborescence complète)
            archive.write(fichier, arcname=fichier.name)

    print(f"\nArchive créée avec succès : {chemin_archive.resolve()}")
    print(f"Taille de l'archive : {chemin_archive.stat().st_size} octets")

    return chemin_archive


if __name__ == "__main__":
    # Test d'archivage sur le répertoire courant '.'
    archiver_fichiers_python(dossier_source=".")
```	

**Chapitre 15 / Exercice 1 
```bash
python -m venv env_projet
source env_projet/bin/activate
deactivate
```	
**Chapitre 15 / Exercice 2
```bash
# 1. Activation de l'environnement
source env_projet/bin/activate

# 2. Vérification de l'exécutable Python actif
which python

# 3. Désactivation de l'environnement
deactivate
```	
**Chapitre 16 / Exercice 1 
```python
from pathlib import Path

def creer_fichier_unicode(nom_fichier: str = "notes.txt") -> None:
    """Crée un fichier texte spécifié avec l'encodage UTF-8

    et y inscrit une phrase contenant des caractères accentués.
    """
    chemin_fichier = Path(nom_fichier)

    # Texte à inscrire contenant divers caractères accentués et spéciaux
    contenu: str = (
        "Apprendre à programmer en Python est une activité très enrichissante !\n"
        "Gérer correctement l'encodage UTF-8 garantit une lisibilité universelle."
    )

    # Ouverture du fichier en mode écriture ("w") avec encodage explicite utf-8
    with open(chemin_fichier, mode="w", encoding="utf-8") as fichier:
        fichier.write(contenu)

    print(f"Le fichier '{chemin_fichier.name}' a été créé avec succès en encodage UTF-8.")


if __name__ == "__main__":
    creer_fichier_unicode()
```	
**Chapitre 16 / Exercice 2
```python
from pathlib import Path

def lire_fichier_unicode(nom_fichier: str = "notes.txt") -> None:
    """Ouvre et lit le contenu global d'un fichier texte au format UTF-8,

    puis l'affiche dans la console.
    """
    chemin_fichier = Path(nom_fichier)

    # Vérification préalable de l'existence du fichier
    if not chemin_fichier.is_file():
        print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
        return

    # Ouverture du fichier en mode lecture ("r") avec encodage UTF-8
    with open(chemin_fichier, mode="r", encoding="utf-8") as fichier:
        contenu: str = fichier.read()

    print(f"--- Contenu de '{chemin_fichier.name}' ---")
    print(contenu)


if __name__ == "__main__":
    lire_fichier_unicode()
```	

**Chapitre 17 / Exercice 1 
```python
class Livre:
    """Représente un livre avec un titre et un auteur."""

    def __init__(self, titre: str, auteur: str) -> None:
        """Initialise les attributs de l'instance Livre."""
        self.titre: str = titre
        self.auteur: str = auteur

    def obtenir_description(self) -> str:
        """Retourne une description textuelle complète de l'ouvrage."""
        return f"« {self.titre} » par {self.auteur}"


if __name__ == "__main__":
    # Instanciation de deux objets Livre
    livre_1 = Livre("Le Comte de Monte-Cristo", "Alexandre Dumas")
    livre_2 = Livre("L'Étranger", "Albert Camus")

    # Appel de la méthode de description
    print(livre_1.obtenir_description())
    print(livre_2.obtenir_description())
```	
**Chapitre 17 / Exercice 2
```python
class Livre:
    """Représente un livre avec un titre et un auteur."""

    def __init__(self, titre: str, auteur: str) -> None:
        self.titre: str = titre
        self.auteur: str = auteur

    def obtenir_description(self) -> str:
        """Retourne une description textuelle de l'ouvrage."""
        return f"« {self.titre} » par {self.auteur}"


class LivreNumerique(Livre):
    """Représente un livre numérique, héritant de Livre,

    avec une propriété supplémentaire pour la taille du fichier.
    """

    def __init__(self, titre: str, auteur: str, taille_mo: float) -> None:
        # Appel du constructeur de la classe parente (Livre)
        super().__init__(titre, auteur)
        # Attribut propre à la classe fille
        self.taille_mo: float = taille_mo

    def obtenir_description(self) -> str:
        """Surcharge de la méthode parente pour inclure la taille du fichier."""
        description_base = super().obtenir_description()
        return f"{description_base} [Ebook - {self.taille_mo} Mo]"


if __name__ == "__main__":
    # Instanciation d'un objet LivreNumerique
    ebook = LivreNumerique("Apprendre Python", "Karim Belhadj", 4.5)

    # Affichage de la description
    print(ebook.obtenir_description())
    print(f"Taille du fichier : {ebook.taille_mo} Mo")
```	
**Chapitre 18 / Exercice 1 
```python
import sqlite3
from pathlib import Path

def initialiser_base_de_donnees(nom_bdd: str = "inventaire.db") -> None:
    """Crée une base de données SQLite, génère la table 'produits'

    et y insère un enregistrement de test avec commit.
    """
    chemin_bdd = Path(nom_bdd)

    # Connexion à la base de données (le fichier est créé s'il n'existe pas)
    with sqlite3.connect(chemin_bdd) as connexion:
        cursor = connexion.cursor()

        # 1. Création de la table produits
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prix REAL NOT NULL
            )
        """)

        # 2. Insertion d'un enregistrement à l'aide de requêtes préparées (?)
        produit_test = ("Clavier mécanique", 89.99)
        cursor.execute("""
            INSERT INTO produits (nom, prix)
            VALUES (?, ?)
        """, produit_test)

        # 3. Validation explicite des modifications
        connexion.commit()

        print(f"Base de données '{chemin_bdd.name}' initialisée avec succès.")
        print(f"Produit ajouté : {produit_test[0]} à {produit_test[1]} €")


if __name__ == "__main__":
    initialiser_base_de_donnees()
```	

**Chapitre 18 / Exercice 2
```python
import sqlite3
from pathlib import Path

def rechercher_produits_par_prix_max(prix_max: float, nom_bdd: str = "inventaire.db") -> None:
    """Récupère et affiche les produits dont le prix est strictement inférieur

    au seuil passé en paramètre.
    """
    chemin_bdd = Path(nom_bdd)

    if not chemin_bdd.is_file():
        print(f"Erreur : La base de données '{chemin_bdd}' est introuvable.")
        return

    # Connexion à la base de données
    with sqlite3.connect(chemin_bdd) as connexion:
        cursor = connexion.cursor()

        # Requête SELECT avec clause WHERE et paramètre sécurisé (?)
        requete = "SELECT id, nom, prix FROM produits WHERE prix < ?"
        cursor.execute(requete, (prix_max,))

        # Récupération de l'ensemble des résultats
        produits = cursor.fetchall()

        print(f"--- Produits dont le prix est inférieur à {prix_max:.2f} € ---")
        
        if not produits:
            print("Aucun produit ne correspond à ce critère.")
            return

        for produit_id, nom, prix in produits:
            print(f"ID: {produit_id} | Nom: {nom:<20} | Prix: {prix:.2f} €")


if __name__ == "__main__":
    # Recherche des produits dont le prix est inférieur à 100.00 €
    rechercher_produits_par_prix_max(100.0)
```	


