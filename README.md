# Test technique en python - data nlp & backend

Ce test est destiné à la fois pour une candidature data et backend.

## Préambule

### Instructions

- la durée du test recommandé est de 2h au total. L'important n'est pas de tout finir, mais de faire un travail de qualité sur ce qui aura été effectué.
- chaque exercice donnera lieu à la création d'un dossier spécifique, qui pourra contenir plusieurs modules python
- il est interdit d'utiliser des bibliothèques extérieures à celles incluses directement dans Python
- il est autorisé d'utiliser Internet, notamment bien sûr pour s'appuyer sur la doc python
- il est conseillé de produire un code modulaire, orienté objet
- toutes les ressources sont fournies en UTF-8 (cloner le repo actuel)
- il est requis d'utiliser git

### Seront jugés

- la qualité des résultats
- l'usage opportun des structures de données
- la complexité des algorithmes
- la simplicité (au sens positif) des algorithmes et du code.

### Résultats

Les résultats, sont attendu dans le repo Github du candidat contenant un dossier par exercice. Chaque dossier contiendra le code source et fichiers générés. Merci de nous partager le lien de votre repo sur axel.schafers@clustaar.com & amin.messaoudi@clustaar.com .

NB : toutes les ressources de ce test sont encodées en UTF-8. Il en est attendu de même du côté du candidat.

## Exercices

### Exercice 1 - échauffement

    Input : le fichier texte.txt, à télécharger.
    Output : afficher les 10 mots porteurs de sens les plus présents dans le fichier, associés à leur fréquence.
    Conseil : utiliser le module blacklist.py.

### Exercice 2 - offline web mining

    Input : les fichiers du dossier html, à télécharger.
    Output : l'affichage pour chaque fichier html d'une structure : Titre, contenu de l'article, liens de l'articles.

### Exercice 3 - indexation

    Input : les fichiers du dossier html, à télécharger.
    Output :
        une classe représentant une page html et ses informations structurées (titre, contenu, liens) avec une méthode to_json(), et les fichiers json résultants.
        un fichier d'index inversé, reliant chaque token des différents pages html aux pages qui les mentionnent.
    Conseil : réutiliser le travail des exercices précédents.

### Exercice 4 - moteur de recherche

    Output : un programme qui prend en entrée un mot, et affiche la liste des articles qui le contiennent de manière structurées.
    Conseil : réutiliser les fichiers produits dans l'exercice 3.

### Exercice 5 - gestion des phrases

    Output : améliorer le programme précédent en permettant à l'utilisateur de fournir une phrase en entrée du moteur de recherche.
    Conseil : cet exercice est à voir comme une surcouche du précédent.

### Exercice 6 (bakend) - API Falcon GET request

    Output : retourner un json au format {data: {xxxx}} le plus adapté
    Conseil : cet exercice est à voir comme une surcouche du précédent avec l'utilisation de falcon. (https://falcon.readthedocs.io/en/stable/).


### Exercice 7 (bakend) - Pytest

    Instruction : faire des tests minimaux sur le handler pour s'assurer du cas de succès, de retour vide et d'erreur.
    Conseil : faire simple ne traiter que les 3 cas présentés. (https://docs.pytest.org/).


### Exercice 8 (devops) - Image docker

    Instruction : ajouter le code dans une image docker et rendre disponible l'api sur le port 4242.
    Conseil : cet exercice est à voir comme une surcouche du précedent. (https://docs.docker.com/engine/reference/commandline/docker/).

### Exercice 9 (devops) - Ngrok

    Instruction : utiliser ngrok en local pour permettre l'utilisation de l'API à distance (https://ngrok.com/).
