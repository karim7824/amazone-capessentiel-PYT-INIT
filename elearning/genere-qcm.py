import os
import json
import zipfile

# Dictionnaire complet des QCM pour les 16 chapitres de la formation Python
qcm_data = {
    "chapitre1": {
        "quiz_title": "Chapitre 1 : Définir et manipuler des données types en mémoire",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Comment déclare-t-on une variable en Python ?",
                "answerOptions": [
                    {"text": "Par simple affectation d'une valeur (ex: x = 5)", "rationale": "Correct", "isCorrect": True},
                    {"text": "En utilisant le mot-clé var", "rationale": "Faux", "isCorrect": False},
                    {"text": "En précisant son type obligatoirement", "rationale": "Faux", "isCorrect": False},
                    {"text": "Avec la commande dim", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Le typage est dynamique en Python."
            },
            {
                "questionNumber": 2,
                "question": "Parmi ces types, lequel est un type de données scalaire ?",
                "answerOptions": [
                    {"text": "list", "rationale": "Faux", "isCorrect": False},
                    {"text": "float", "rationale": "Correct", "isCorrect": True},
                    {"text": "dict", "rationale": "Faux", "isCorrect": False},
                    {"text": "set", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Les scalaires représentent des valeurs uniques non décomposables."
            },
            {
                "questionNumber": 3,
                "question": "Quelle structure de données agrégée est immuable ?",
                "answerOptions": [
                    {"text": "list", "rationale": "Faux", "isCorrect": False},
                    {"text": "dict", "rationale": "Faux", "isCorrect": False},
                    {"text": "tuple", "rationale": "Correct", "isCorrect": True},
                    {"text": "set", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Il s'utilise avec des parenthèses."
            }
        ]
    },
    "chapitre2": {
        "quiz_title": "Chapitre 2 : Les opérateurs",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Que réalise l'opérateur d'affectation augmentée `+=` ?",
                "answerOptions": [
                    {"text": "Il compare deux variables", "rationale": "Faux", "isCorrect": False},
                    {"text": "Il ajoute une valeur à la variable et stocke le résultat", "rationale": "Correct", "isCorrect": True},
                    {"text": "Il élève au carré", "rationale": "Faux", "isCorrect": False},
                    {"text": "Il convertit la variable en texte", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Équivalent à x = x + y."
            },
            {
                "questionNumber": 2,
                "question": "Quel opérateur retourne le reste d'une division entière ?",
                "answerOptions": [
                    {"text": "/", "rationale": "Faux", "isCorrect": False},
                    {"text": "//", "rationale": "Faux", "isCorrect": False},
                    {"text": "%", "rationale": "Correct", "isCorrect": True},
                    {"text": "**", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Aussi appelé modulo."
            }
        ]
    },
    "chapitre3": {
        "quiz_title": "Chapitre 3 : Convertir les données - casting ou transtypage",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quelle fonction permet de convertir explicitement une chaîne en entier ?",
                "answerOptions": [
                    {"text": "str()", "rationale": "Faux", "isCorrect": False},
                    {"text": "int()", "rationale": "Correct", "isCorrect": True},
                    {"text": "float()", "rationale": "Faux", "isCorrect": False},
                    {"text": "char()", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Nommé d'après le type entier."
            },
            {
                "questionNumber": 2,
                "question": "Que se passe-t-il lors de l'opération 3 + 4.5 ?",
                "answerOptions": [
                    {"text": "Une erreur de type", "rationale": "Faux", "isCorrect": False},
                    {"text": "Une conversion implicite de l'entier en flottant", "rationale": "Correct", "isCorrect": True},
                    {"text": "Une conversion explicite obligatoire", "rationale": "Faux", "isCorrect": False},
                    {"text": "La conversion du flottant en entier", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Python gère automatiquement les types mixtes numériques."
            }
        ]
    },
    "chapitre4": {
        "quiz_title": "Chapitre 4 : Manipulation des chaines de caractères",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quelle méthode est recommandée pour insérer des variables dans une chaîne de manière lisible ?",
                "answerOptions": [
                    {"text": "Les f-strings", "rationale": "Correct", "isCorrect": True},
                    {"text": "La concaténation avec + uniquement", "rationale": "Faux", "isCorrect": False},
                    {"text": "L'opérateur %", "rationale": "Faux", "isCorrect": False},
                    {"text": "join()", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Elles préfixent la chaîne par la lettre f."
            },
            {
                "questionNumber": 2,
                "question": "Quel module standard permet d'utiliser des expressions régulières ?",
                "answerOptions": [
                    {"text": "string", "rationale": "Faux", "isCorrect": False},
                    {"text": "regex", "rationale": "Faux", "isCorrect": False},
                    {"text": "re", "rationale": "Correct", "isCorrect": True},
                    {"text": "pattern", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Son nom est très court (deux lettres)."
            }
        ]
    },
    "chapitre5": {
        "quiz_title": "Chapitre 5 : Manipulation des données structurées - list, dict et set",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quelle méthode sécurisée permet d'interroger un dictionnaire sans lever d'erreur si la clé est absente ?",
                "answerOptions": [
                    {"text": "get()", "rationale": "Correct", "isCorrect": True},
                    {"text": "find()", "rationale": "Faux", "isCorrect": False},
                    {"text": "search()", "rationale": "Faux", "isCorrect": False},
                    {"text": "fetch()", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Elle accepte une valeur de repli par défaut."
            },
            {
                "questionNumber": 2,
                "question": "Quelle est la principale caractéristique d'un ensemble (`set`) ?",
                "answerOptions": [
                    {"text": "Il conserve l'ordre d'insertion", "rationale": "Faux", "isCorrect": False},
                    {"text": "Il supprime automatiquement les doublons", "rationale": "Correct", "isCorrect": True},
                    {"text": "Il est indexé par des clés numériques", "rationale": "Faux", "isCorrect": False},
                    {"text": "Il est strictement immuable", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Idéal pour l'unicité et les opérations ensemblistes."
            }
        ]
    },
    "chapitre6": {
        "quiz_title": "Chapitre 6 : Les instructions contrôles",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quelle instruction réalise un filtrage par motif (*pattern matching*) en Python ?",
                "answerOptions": [
                    {"text": "switch", "rationale": "Faux", "isCorrect": False},
                    {"text": "match", "rationale": "Correct", "isCorrect": True},
                    {"text": "select", "rationale": "Faux", "isCorrect": False},
                    {"text": "check", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Introduite dans les versions récentes du langage."
            },
            {
                "questionNumber": 2,
                "question": "À quoi sert la fonction `zip()` combinée avec une boucle `for` ?",
                "answerOptions": [
                    {"text": "À compresser des fichiers", "rationale": "Faux", "isCorrect": False},
                    {"text": "À parcourir simultanément plusieurs collections", "rationale": "Correct", "isCorrect": True},
                    {"text": "À inverser une liste", "rationale": "Faux", "isCorrect": False},
                    {"text": "À trier des dictionnaires", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Elle assemble des éléments sous forme de tuples."
            }
        ]
    },
    "chapitre7": {
        "quiz_title": "Chapitre 7 : Les fonctions et passage d'arguments",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Que permet de capturer la syntaxe `*args` dans une fonction ?",
                "answerOptions": [
                    {"text": "Un nombre variable d'arguments positionnels sous forme de tuple", "rationale": "Correct", "isCorrect": True},
                    {"text": "Un dictionnaire d'arguments nommés", "rationale": "Faux", "isCorrect": False},
                    {"text": "Uniquement une liste", "rationale": "Faux", "isCorrect": False},
                    {"text": "Des valeurs constantes", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Utilise un astérisque pour les arguments positionnels."
            },
            {
                "questionNumber": 2,
                "question": "Quel mot-clé est utilisé pour déclarer une fonction anonyme sur une seule ligne ?",
                "answerOptions": [
                    {"text": "def", "rationale": "Faux", "isCorrect": False},
                    {"text": "lambda", "rationale": "Correct", "isCorrect": True},
                    {"text": "func", "rationale": "Faux", "isCorrect": False},
                    {"text": "anon", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Nom issu du calcul lambda."
            }
        ]
    },
    "chapitre8": {
        "quiz_title": "Chapitre 8 : Traiter une masse de données",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quelle fonction applique une transformation à tous les éléments d'une collection ?",
                "answerOptions": [
                    {"text": "filter()", "rationale": "Faux", "isCorrect": False},
                    {"text": "map()", "rationale": "Correct", "isCorrect": True},
                    {"text": "reduce()", "rationale": "Faux", "isCorrect": False},
                    {"text": "sort()", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Mappe une fonction sur un itérable."
            },
            {
                "questionNumber": 2,
                "question": "Dans quel module faut-il importer la fonction `reduce()` ?",
                "answerOptions": [
                    {"text": "math", "rationale": "Faux", "isCorrect": False},
                    {"text": "os", "rationale": "Faux", "isCorrect": False},
                    {"text": "functools", "rationale": "Correct", "isCorrect": True},
                    {"text": "itertools", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Module dédié aux outils fonctionnels."
            }
        ]
    },
    "chapitre9": {
        "quiz_title": "Chapitre 9 : Les générateurs",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quelle instruction permet à une fonction de retourner une valeur tout en suspendant son état ?",
                "answerOptions": [
                    {"text": "return", "rationale": "Faux", "isCorrect": False},
                    {"text": "yield", "rationale": "Correct", "isCorrect": True},
                    {"text": "pause", "rationale": "Faux", "isCorrect": False},
                    {"text": "wait", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Caractéristique clé des générateurs."
            },
            {
                "questionNumber": 2,
                "question": "Quel est l'avantage principal d'un générateur par rapport à une liste classique ?",
                "answerOptions": [
                    {"text": "Il stocke toutes les données en mémoire vive", "rationale": "Faux", "isCorrect": False},
                    {"text": "Il produit les valeurs à la demande pour économiser la mémoire", "rationale": "Correct", "isCorrect": True},
                    {"text": "Il est modifiable indéfiniment", "rationale": "Faux", "isCorrect": False},
                    {"text": "Il trie automatiquement les données", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Évaluation paresseuse (*lazy evaluation*)."
            }
        ]
    },
    "chapitre10": {
        "quiz_title": "Chapitre 10 : Un code plus robuste en prenant en compte les erreurs",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quel mot-clé est utilisé en Python pour émettre (lever) une exception volontairement ?",
                "answerOptions": [
                    {"text": "throw", "rationale": "Faux", "isCorrect": False},
                    {"text": "raise", "rationale": "Correct", "isCorrect": True},
                    {"text": "except", "rationale": "Faux", "isCorrect": False},
                    {"text": "panic", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Terme anglais signifiant soulever/lever."
            },
            {
                "questionNumber": 2,
                "question": "À quoi sert le bloc `finally` dans une gestion d'exceptions ?",
                "answerOptions": [
                    {"text": "À s'exécuter systématiquement à la fin, qu'il y ait une erreur ou non", "rationale": "Correct", "isCorrect": True},
                    {"text": "Uniquement en cas de succès", "rationale": "Faux", "isCorrect": False},
                    {"text": "À ignorer toutes les erreurs", "rationale": "Faux", "isCorrect": False},
                    {"text": "À relancer le programme", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Idéal pour la libération de ressources."
            }
        ]
    },
    "chapitre11": {
        "quiz_title": "Chapitre 11 : Script python en ligne de commande et passage d'arguments",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quelle condition vérifie si un script est exécuté directement comme programme principal ?",
                "answerOptions": [
                    {"text": "if __name__ == '__main__':", "rationale": "Correct", "isCorrect": True},
                    {"text": "if script.main():", "rationale": "Faux", "isCorrect": False},
                    {"text": "if run == true:", "rationale": "Faux", "isCorrect": False},
                    {"text": "if __file__ == active:", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Utilise des variables magiques soulignées."
            },
            {
                "questionNumber": 2,
                "question": "Quel module standard gère les arguments passés en ligne de commande sous forme de liste ?",
                "answerOptions": [
                    {"text": "os", "rationale": "Faux", "isCorrect": False},
                    {"text": "sys", "rationale": "Correct", "isCorrect": True},
                    {"text": "argparse", "rationale": "Faux", "isCorrect": False},
                    {"text": "terminal", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Fournit l'accès à sys.argv."
            }
        ]
    },
    "chapitre12": {
        "quiz_title": "Chapitre 12 : Gestion des package - import et création",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quel outil officiel permet d'installer des packages tiers depuis PyPI ?",
                "answerOptions": [
                    {"text": "npm", "rationale": "Faux", "isCorrect": False},
                    {"text": "pip", "rationale": "Correct", "isCorrect": True},
                    {"text": "cargo", "rationale": "Faux", "isCorrect": False},
                    {"text": "gem", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Gestionnaire de paquets par défaut de Python."
            },
            {
                "questionNumber": 2,
                "question": "Quel module standard permet de manipuler la compression de données ?",
                "answerOptions": [
                    {"text": "zlib", "rationale": "Correct", "isCorrect": True},
                    {"text": "zipfile", "rationale": "Faux", "isCorrect": False},
                    {"text": "tar", "rationale": "Faux", "isCorrect": False},
                    {"text": "compress", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Basé sur la bibliothèque de compression du même nom."
            }
        ]
    },
    "chapitre13": {
        "quiz_title": "Chapitre 13 : Environnement virtuel adapté à chaque application",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quel module natif permet de créer un contexte Python isolé ?",
                "answerOptions": [
                    {"text": "virtualenv", "rationale": "Faux", "isCorrect": False},
                    {"text": "venv", "rationale": "Correct", "isCorrect": True},
                    {"text": "isolation", "rationale": "Faux", "isCorrect": False},
                    {"text": "env", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Intégré directement dans la bibliothèque standard."
            },
            {
                "questionNumber": 2,
                "question": "Quelle commande permet d'activer l'environnement virtuel sous Linux/macOS ?",
                "answerOptions": [
                    {"text": "source .venv/bin/activate", "rationale": "Correct", "isCorrect": True},
                    {"text": "activate.bat", "rationale": "Faux", "isCorrect": False},
                    {"text": "run venv", "rationale": "Faux", "isCorrect": False},
                    {"text": "init .venv", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Utilise la commande de shell standard."
            }
        ]
    },
    "chapitre14": {
        "quiz_title": "Chapitre 14 : Gestion des fichiers et des répertoires",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quel argument faut-il systématiquement privilégier lors de l'ouverture d'un fichier texte pour la portabilité ?",
                "answerOptions": [
                    {"text": "encoding='utf-8'", "rationale": "Correct", "isCorrect": True},
                    {"text": "mode='binary'", "rationale": "Faux", "isCorrect": False},
                    {"text": "unicode=True", "rationale": "Faux", "isCorrect": False},
                    {"text": "format='text'", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Garantit la gestion correcte des accents."
            },
            {
                "questionNumber": 2,
                "question": "Quel gestionnaire de contexte garantit la fermeture automatique d'un fichier ?",
                "answerOptions": [
                    {"text": "using", "rationale": "Faux", "isCorrect": False},
                    {"text": "with", "rationale": "Correct", "isCorrect": True},
                    {"text": "open", "rationale": "Faux", "isCorrect": False},
                    {"text": "managed", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Mot-clé suivi de l'instruction open()."
            }
        ]
    },
    "chapitre15": {
        "quiz_title": "Chapitre 15 : Programmation orientée objets",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quel paramètre représente obligatoirement l'instance courante dans les méthodes d'une classe ?",
                "answerOptions": [
                    {"text": "this", "rationale": "Faux", "isCorrect": False},
                    {"text": "self", "rationale": "Correct", "isCorrect": True},
                    {"text": "instance", "rationale": "Faux", "isCorrect": False},
                    {"text": "base", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Convention de nommage universelle en Python."
            },
            {
                "questionNumber": 2,
                "question": "Quel nom porte la méthode spéciale servant de constructeur de classe ?",
                "answerOptions": [
                    {"text": "__init__", "rationale": "Correct", "isCorrect": True},
                    {"text": "__create__", "rationale": "Faux", "isCorrect": False},
                    {"text": "__new__", "rationale": "Faux", "isCorrect": False},
                    {"text": "__start__", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "S'exécute automatiquement à l'instanciation."
            }
        ]
    },
    "chapitre16": {
        "quiz_title": "Chapitre 16 : Accès aux bases de données",
        "questions": [
            {
                "questionNumber": 1,
                "question": "Quel module standard est intégré pour manipuler des bases de données légères en Python ?",
                "answerOptions": [
                    {"text": "mysql", "rationale": "Faux", "isCorrect": False},
                    {"text": "sqlite3", "rationale": "Correct", "isCorrect": True},
                    {"text": "pgdb", "rationale": "Faux", "isCorrect": False},
                    {"text": "sqlclient", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Basé sur un moteur SQL sans serveur."
            },
            {
                "questionNumber": 2,
                "question": "Quelle instruction permet de valider définitivement une transaction en base de données ?",
                "answerOptions": [
                    {"text": "save()", "rationale": "Faux", "isCorrect": False},
                    {"text": "commit()", "rationale": "Correct", "isCorrect": True},
                    {"text": "flush()", "rationale": "Faux", "isCorrect": False},
                    {"text": "apply()", "rationale": "Faux", "isCorrect": False}
                ],
                "hint": "Sécurise les modifications apportées par le curseur."
            }
        ]
    }
}

zip_filename = "qcm_formation.zip"

# Création du fichier zip et écriture des fichiers qcm.json par dossier de chapitre
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as qcm_zip:
    for folder_name, content in qcm_data.items():
        # Sérialisation JSON propre avec indentation et support de l'utf-8 sans échappement des accents
        json_content = json.dumps(content, ensure_ascii=False, indent=2)
        
        # Construction du chemin cible dans l'archive (ex: chapitre1/qcm.json)
        arc_path = os.path.join(folder_name, "qcm.json")
        
        # Ajout du fichier dans l'archive zip
        qcm_zip.writestr(arc_path, json_content)

print(f"L'archive '{zip_filename}' a été générée avec succès pour l'ensemble des 16 chapitres.")