# Chapitre 16 : Gestion des fichiers et des répertoires

La gestion des fichiers et des répertoires permet d'interagir directement avec le système de stockage pour enregistrer et restituer des informations. Maîtriser ces concepts est indispensable pour persister l'état de vos applications.
Dans ce chapitre :

* Concepts généraux sur les streams et fichiers


* Créer un fichier texte en unicode : ouverture, écriture et lecture



---

## Concepts généraux sur les streams et fichiers

Les streams (flux) représentent des canaux de communication séquentiels permettant de transférer des données entre la mémoire vive et des périphériques de stockage ou des fichiers. Ils garantissent un traitement fluide et ordonné des flux d'informations.

```python
# Illustration conceptuelle du traitement par flux
flux_donnees = "Lecture ou écriture séquentielle"

```

> 💡 Considérez toujours un fichier ouvert comme un flux unidirectionnel ou bidirectionnel nécessitant une clôture rigoureuse après utilisation.

---

## Créer un fichier text en unicode - ouvrir, ecrire, lire

La création d'un fichier texte en encodage Unicode garantit la prise en charge universelle des caractères accentués et des symboles internationaux. Les fonctions natives permettent d'ouvrir, d'écrire et de lire ces contenus en toute sécurité.

```python
# Création, écriture et lecture d'un fichier texte en UTF-8
with open("document.txt", "w", encoding="utf-8") as f:
    f.write("Texte en Unicode avec des accents : é, à, ê.")

with open("document.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

```

> 💡 Spécifiez systématiquement l'argument `encoding="utf-8"` lors de l'ouverture de fichiers texte pour éviter les erreurs de décodage selon les systèmes d'exploitation.

---

## Exemple de synthèse

```python
# Programme complet combinant les concepts de streams et la gestion de fichiers Unicode

nom_fichier = "message_unicode.txt"

# 1. Écriture dans un fichier texte en Unicode
with open(nom_fichier, "w", encoding="utf-8") as fichier_sortie:
    fichier_sortie.write("Bonjour Karim !\n")
    fichier_sortie.write("Apprentissage de la gestion des flux et fichiers en Python.\n")

# 2. Lecture du fichier texte via un flux sécurisé
with open(nom_fichier, "r", encoding="utf-8") as fichier_entree:
    for numero_ligne, ligne in enumerate(fichier_entree, start=1):
        print(f"Ligne {numero_ligne} : {ligne.strip()}")

```

### Exercices de fin de chapitre

1. **Exercice 1 :** Écrivez un script qui crée un fichier texte nommé `notes.txt` en encodage Unicode, puis y inscrit une phrase comportant des caractères accentués.
2. **Exercice 2 :** Ouvrez le fichier `notes.txt` en mode lecture avec l'encodage approprié, lisez son contenu global et affichez-le dans la console.
