# Chapitre 18 : La programmation asynchrone avec `asyncio`

La gestion efficace des opérations d'entrée/sortie (E/S) — comme l'accès au réseau, aux bases de données ou au système de fichiers — est cruciale pour concevoir des applications Python performantes. Dans ce chapitre, vous découvrirez les principes de la programmation asynchrone non bloquante. Vous apprendrez à utiliser le module standard `asyncio` pour exécuter plusieurs tâches de manière concurrente sans avoir recours au multithreading complexe.

* Les différences fondamentales entre l'exécution synchrone bloquante et asynchrone non bloquante
* Les coroutines, les objets `Future`/`Task` et la syntaxe `async` / `await`
* Le rôle essentiel de la boucle d'événements (*event loop*)
* La planification et le regroupement de tâches concurrentes avec `asyncio.gather()` et `asyncio.TaskGroup`

---

## Appels non bloquants et concurrents

En programmation synchrone (classique), lorsqu'un programme effectue une opération d'E/S (comme télécharger une page web), le fil d'exécution reste bloqué en attendant la réponse. Durant cet intervalle, le processeur ne traite aucune autre instruction.

L'approche **asynchrone et non bloquante** permet de libérer le fil d'exécution pendant ces temps d'attente : dès qu'une tâche s'interrompt pour attendre un résultat externe, le programme passe immédiatement à l'exécution d'une autre tâche.

```python
import time

# Exemple synchrone (bloquant) : les tâches s'exécutent en séquence
def tache_synchrone(nom, duree):
    print(f"Début de la tâche {nom}")
    time.sleep(duree)  # Bloque tout le programme pendant 'duree' secondes
    print(f"Fin de la tâche {nom}")

tache_synchrone("A", 2)
tache_synchrone("B", 1)
# Temps total d'exécution : 3 secondes

```

> 💡 **Note**
> La concurrence n'est pas le parallélisme. La concurrence gère plusieurs tâches en alternance sur un seul thread (idéal pour les opérations dépendantes du réseau/E/S), tandis que le parallélisme exécute plusieurs calculs simultanément sur plusieurs cœurs processeur (idéal pour les calculs intenses).

---

## Promise ou Future avec async, await

En Python, une fonction asynchrone se définit avec le mot-clé `async def` et produit une **coroutine**. Pour suspendre l'exécution d'une coroutine et céder le contrôle au moteur asynchrone, on utilise le mot-clé `await`.

Les objets sous-jacents gérant ces opérations différées s'appellent des **Futures** (ou **Tasks** quand ils enveloppent une coroutine). Une *Future* représente un résultat qui n'est pas encore disponible, mais qui le sera plus tard.

```python
import asyncio

async def telecharger_donnees(id_requete):
    print(f"Ressource {id_requete} : téléchargement démarré...")
    # asyncio.sleep simule une attente I/O non bloquante
    await asyncio.sleep(2)
    print(f"Ressource {id_requete} : téléchargement terminé.")
    return {"id": id_requete, "statut": "OK"}

async def main():
    # 'await' attend la résolution de la coroutine sans bloquer le reste de la boucle
    resultat = await telecharger_donnees(101)
    print("Résultat obtenu :", resultat)

# Exécution de la coroutine principale
asyncio.run(main())

```

> ⚠️ **Piège**
> N'utilisez jamais `time.sleep()` à l'intérieur d'une coroutine asynchrone. Cela bloquerait la boucle d'événements tout entière. Utilisez toujours sa variante asynchrone : `await asyncio.sleep()`.

---

## La boucle d'événements (`event loop`)

La **boucle d'événements** (*event loop*) est le cœur réactif du système `asyncio`. Elle maintient la liste de toutes les tâches en cours, surveille leur état (en attente, prêtes, terminées) et distribue le temps de processeur au fur et à mesure que les événements se produisent.

Depuis Python 3.7, la fonction `asyncio.run()` gère automatiquement la création, l'exécution et la fermeture propre de la boucle d'événements.

```python
import asyncio

async def notifier_utilisateur():
    print("Notification envoyée à l'utilisateur.")

async def main():
    # Obtenir la référence de la boucle d'événements courante
    loop = asyncio.get_running_loop()
    print(f"Boucle d'événements active : {loop}")
    
    # Création d'une tâche explicite liée à la boucle
    tache = loop.create_task(notifier_utilisateur())
    await tache

# asyncio.run() initialise et ferme la boucle automatiquement
asyncio.run(main())

```

> Privilégiez l'utilisation de `asyncio.run(main())` comme point d'entrée de votre application au lieu de manipuler directement la boucle avec `get_event_loop()` ou `loop.run_until_complete()`.

---

## Gestion des tâches concurrentes

Pour tirer le plein potentiel de l'asynchronisme, il est essentiel d'exécuter plusieurs coroutines en parallèle. `asyncio` propose plusieurs mécanismes pour orchestrer et regrouper ces tâches.

**Utilisation de `asyncio.gather()`**

`asyncio.gather()` permet de lancer plusieurs coroutines simultanément et de collecter leurs résultats dans une liste ordonnée.

```python
import asyncio
import time

async def traiter_commande(id_commande, delai):
    await asyncio.sleep(delai)
    return f"Commande {id_commande} traitée en {delai}s"

async def main():
    debut = time.perf_counter()
    
    # Lancement concurrent de 3 commandes
    resultats = await asyncio.gather(
        traiter_commande(1, 2),
        traiter_commande(2, 1),
        traiter_commande(3, 3)
    )
    
    fin = time.perf_counter()
    print("Résultats :", resultats)
    print(f"Temps total d'exécution : {fin - debut:.2f} secondes")

asyncio.run(main())

```

Pour exécuter ce script depuis votre terminal :

```bash
python script_async.py

```

**Utilisation moderne avec `asyncio.TaskGroup`**

À partir de Python 3.11, l'utilisation de `asyncio.TaskGroup` est recommandée pour une gestion plus sûre des exceptions (gestion contextuelle d'erreurs concurrentes via les *Exception Groups*).

```python
import asyncio

async def service_a():
    await asyncio.sleep(1)
    print("Service A prêt")

async def service_b():
    await asyncio.sleep(1.5)
    print("Service B prêt")

async def main():
    # Le bloc TaskGroup garantit que toutes les tâches terminent ou sont annulées proprement en cas d'erreur
    async with asyncio.TaskGroup() as tg:
        tg.create_task(service_a())
        tg.create_task(service_b())
    
    print("Tous les services sont opérationnels.")

asyncio.run(main())

```

---

### Exercices de fin de chapitre

Dans ce chapitre, vous avez découvert les mécanismes de l'exécution asynchrone en Python grâce au module `asyncio`. Vous avez appris à définir des coroutines avec `async` et `await`, à planifier leur exécution au sein de la boucle d'événements, ainsi qu'à gérer plusieurs appels non bloquants en parallèle à l'aide de `asyncio.gather` et `TaskGroup`.

**Exercice 1 : traitement concurents **
Créez deux coroutines t1() et t2() qui simulent un traitement en attendant des durées différentes (ex: 1s et 3s avec asyncio.sleep).
Chaque coroutine doit afficher un message d'exécution et retourner la chaîne "fin de traitement".
Exécutez-les de manière concurrente avec asyncio.gather() puis affichez leurs valeurs de retour.

**Exercice 2 : traitement concurents avec une exception de délai dépassé, exception asyncio.TimeoutError**
Reprenez les coroutines t1() et t2() de l'exercice précédent.
Exécutez la tâche la plus longue en la limitant avec asyncio.wait_for(..., timeout=2.0).
Interceptez l'exception asyncio.TimeoutError à l'aide d'un bloc try/except pour afficher un message d'erreur lorsque le délai maximal est dépassé.
