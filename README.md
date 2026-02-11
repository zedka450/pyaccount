Pyaccount (ou Pyacnt)

Pyaccount est une extension Python permettant de gérer des profils : créer, connecter, supprimer, et saluer des utilisateurs facilement.

------------------------------------------------------------------

Comment utiliser Pyaccount ?

1️⃣ Télécharger Pyaccount:

Cliquez sur le bouton Code à gauche de la section About du repo GitHub.
Dans le menu déroulant, cliquez sur Download ZIP tout en bas.
Dézippez le fichier téléchargé.

2️⃣ Placer vos fichiers:

Placez votre script Python à côté du fichier pyaccount.py.

3️⃣ Importer Pyaccount dans votre code:

`import pyaccount`
En heut du code.

Commandes principales:
-Créer un compte

`pyaccount.enter(NAME, PASSWORD)`

Remplacez NAME par le nom du compte et PASSWORD par le mot de passe.

-Supprimer un compte

`pyaccount.exit(NAME)`
⚠️ Le compte doit être connecté pour pouvoir le supprimer.

-Se connecter à un compte

`pyaccount.connect(NAME, PASSWORD)`

Remplacez NAME et PASSWORD par le nom et le mot de passe du compte.

-Afficher un message de bienvenue

`pyaccount.welcome(NAME)`
⚠️ Le compte doit être connecté pour que le message s’affiche.

---------------------------------------------------------------------------

💡 Astuce : Les mots de passe sont sécurisés grâce au hash SHA-256, donc même si quelqu’un accède à ton fichier JSON, ils ne pourront pas voir les mots de passe en clair.
⚠️ Le compte doit être connecté pour que le message s’affiche.

💡 Astuce : Les mots de passe sont sécurisés grâce au hash SHA-256, donc même si quelqu’un accède à ton fichier JSON, ils ne pourront pas voir les mots de passe en clair.
