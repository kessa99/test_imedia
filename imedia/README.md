## Q1- Quelle est la différence entre une image Docker et un container ?

### Définition

**Image**: Photo figée et réutilisable de  l'application

**Layers**: Chaque instruction Dockerfile = une couche cachée

**Immuabilité**: Une image ne change jamais après sa création

**Container**: L'image en train de vivre, avec un filesystem temporaire

**Filesystem éphémère**: Tout ce qu'écrit le container disparaît à l'arrêt

### L'analogie

Pense à une **recette de cuisine** et un **plat cuisiné** :
```
Image Docker  =  La recette      => figée, ne change pas, réutilisable
Container     =  Le plat cuisiné => vivant, temporaire, consommable
```

Tu peux cuisiner **100 plats** à partir d'une seule recette. De la même façon, tu peux lancer **100 containers** à partir d'une seule image.

```
Une **image Docker** c'est une photo figée de l'application  elle contient le code, les dépendances, et une configuration. Elle ne change jamais une fois créée, c'est ce qu'on appelle l'immuabilité. Elle est construite en couches superposées, chaque instruction du Dockerfile ajoute une couche. Si on changes seulement le code, Docker réutilise les couches précédentes depuis le cache et va plus vite.

Un **container** c'est cette image en train de tourner. Quand on le démarres, Docker ajoute une couche d'écriture temporaire par dessus l'image. Tout ce qui est écrit pendant l'exécution  logs, fichiers temporaires  disparaît quand le container s'arrête. C'est le filesystem éphémère. L'image en dessous reste intacte. On peux lancer 100 containers depuis la même image, comme cuisiner 100 plats depuis la même recette.
```

## Q2  Quelle est la différence entre CMD et ENTRYPOINT dans un Dockerfile ?

### cmd: la commande apr defaut
c'est la commande qui se lance quand l'on demarres un container. C'est un peut comme un rglage par défaut.

```dockerfile
CMD ["python", "app.py"]
```

### entrypoint:
c'est le programme qui tourne toujours dans le container. c'est un eu comme le coeur du container.

```dockerfile
ENTRYPOINT ["python", "app.py"]
```

## Q3  Comment sécurisez-vous un pipeline CI/CD ?
```
### 1. Ne jamais mettre de secret dans le code
Un secret dans le code = une fuite potentielle dès le premier commit. Tous les mots de passe, tokens et clés API doivent vivre dans le gestionnaire de secrets de ton outil CI/CD, jamais dans un fichier.

## 2. Scanner les vulnérabilités de l'image Docker
Une image Docker peut contenir des failles connues dans ses dépendances ou dans l'OS de base. Un scanner détecte ces failles avant que l'image parte en production.

## 3. Limiter les droits d'accès, principe du moindre privilège
Chaque job du pipeline ne doit avoir accès qu'à ce dont il a strictement besoin. Un job qui fait tourner les tests n'a pas besoin d'accéder à Docker Hub.

## 4. Épingler les versions des actions et images
Utiliser @latest ou @main pour les actions tierces est dangereux, quelqu'un peut modifier l'action et injecter du code malveillant dans ton pipeline sans que tu le saches.

## 5. Scanner le code source SAST
Avant même de construire l'image, analyser le code source pour détecter des failles de sécurité connues comme des injections SQL, des mots de passe codés en dur, ou des dépendances vulnérables.

```

## Q4  Comment gérez-vous les environnements dev, staging et production ?

### Regardons d'abord comment ça marche

Ce sont trois versions de ton application qui tournent en parallèle, chacune avec un rôle précis :

```
Dev        ==>  ton ordinateur, tu codes et testes librement
Staging    ==>  une copie de la prod, tu valides avant de livrer
Production ==>  ce que tes utilisateurs utilisent vraiment
```

On ne touche jamais directement à `main` ou `production`. Tout passe par une Pull Request.

---

### Les variables d'environnement, la seule chose qui change

Le code est identique partout. Ce qui change c'est uniquement la configuration :

| Variable | Dev | Staging | Production |
|---|---|---|---|
| `DEBUG` | true | false | false |
| `DB_PASSWORD` | simple | moyen | très fort |
| `LOG_LEVEL` | debug | info | warning |

Tu as un fichier `.env` différent pour chaque environnement  jamais commité sur Git.

---

### Le voyage d'une fonctionnalité

```
1. Tu codes sur ta machine en local
         
2. Tu pousses les tests se lancent automatiquement
         
3. Tu ouvres une Pull Request vers main
         
4. La PR est mergée déploiement automatique en staging
         
5. Tu valides que tout fonctionne sur staging
         
6. Tu crées un tag  git tag v1.0.0   déploiement en production
```

## Q5  Un container redémarre en boucle en production. Quelle est votre démarche de diagnostic ?

## Container qui redémarre en boucle  Comment diagnostiquer

### La démarche dans l'ordre

---

**Étape 1: Constater le problème**

La première chose c'est de voir ce qui se passe :

```bash
docker ps
```

l'on verras quelque chose comme :
```
CONTAINER ID   STATUS
abc123         Restarting (1) 2 seconds ago   ← il redémarre en boucle
```

Le chiffre entre parenthèses c'est le **code de sortie**  c'est le premier indice.

---

**Étape 2: Lire les logs**

C'est là que l'on trouveras la cause dans 90% des cas :

```bash
docker logs abc123
docker logs abc123 --tail=50
```

Ce que l'on cherches dans les logs :

| Ce qu'on vois | Ce que ça signifie |
|---|---|
| `Connection refused` | L'app ne peut pas joindre la base de données |
| `Port already in use` | Le port est déjà utilisé par autre chose |
| `Module not found` | Une dépendance manque dans l'image |
| `Permission denied` | Problème de droits sur un fichier |
| `Environment variable missing` | Une variable d'env n'est pas définie |

---

**Étape 3: Regarder l'historique des redémarrages**

```bash
docker inspect abc123
```

On cherches cette partie :
```json
"RestartCount": 5,
"State": {
    "ExitCode": 1,      ← 0 = normal, autre chose = erreur
    "Error": "..."      ← le message d'erreur
}
```

---

**Étape 4: Entrer dans le container pour investiguer**

Si les logs ne suffisent pas, On rentres directement dedans :

Si le container tourne encore brièvement
```bash
docker exec -it abc123 bash

docker run -it --entrypoint bash mon-api
```

De là on peux vérifier manuellement si les fichiers sont là, si les variables sont définies, si la DB est joignable.

---

**Étape 5: Vérifier les ressources**

Parfois le container redémarre parce qu'il manque de mémoire :

```bash
docker stats abc123
```

Si la mémoire est à 100% juste avant chaque redémarrage: c'est la cause.

---

### Les causes les plus fréquentes en production

```
Le container redémarre ?
        
Les logs disent "Connection refused"
==> La base de données n'est pas encore prête
==> Solution : ajouter un healthcheck + depends_on dans docker-compose

Les logs disent "variable not found"
==> Un fichier .env manque ou une variable n'est pas définie
==> Solution : vérifier les secrets et le fichier .env

Les logs disent "Permission denied"
==> L'utilisateur dans le container n'a pas les droits
==> Solution : vérifier le USER dans le Dockerfile

Pas de logs du tout
==> Le container plante avant même de démarrer
 Solution : docker run -it --entrypoint bash pour inspecter
```

---

La règle d'or : **les logs d'abord, toujours**. Dans la grande majorité des cas la réponse est là.