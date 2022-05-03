
.. role:: text-bold

Comment ça marche
=================

Pré-requis
----------
Avoir python d'installé
versions 3.7, 3.8, 3.9 or 3.10

Installation
------------

:text-bold:`Installation du package`
::
    pip install --user -U nltk


:text-bold:`Installation des modèles et des datasets prédéfinis`
::
    #en ligne de commande
    
    python -m nltk.downloader popular

    #ou dans un notebook
    
    nltk.download('popular')



.. figure:: ./Images/nltk_ide.png

Utiliser NTLK
--------------

:text-bold:`Import de bibliothèques ou méthodes, classes, modules`
::
    import nltk

    #où l'une de ses méthodes 

    from nltk.stem.snowball import SnowballStemmer
    from nltk.probability import FreqDist
    from nltk.tokenize import word_tokenize


NLTK possède aussi un corpus de textes très fourni pour entraîner ses propres modèles.
::
    from nltk.corpus import hamlet

Principes
---------

- Pré-traitement : une étape qui cherche à standardiser du texte afin de rendre son usage plus facile.
- Représentation du texte comme un vecteur : cette étape peut être effectuée via des techniques de sacs de mots (Bag of Words) ou Term Frequency-Inverse Document Frequency (Tf-IdF). On peut également apprendre des représentations vectorielles (embedding) par apprentissage profond.
- Classification, trouver la phrase la plus similaire… (optionnel)


.. figure:: ./Images/schema.png


Méthode (Orthodoxie) :
----------------------

L'orthodoxie linguistique informatique, après le concile de Californie de 1260, sous le patronage oecuménique des représentants de la Vraie Religion (Python) ainsi que des autres hérésies tolérées (R, Ruby, Pascal, C+, etc.), et après acceptation du phonème comme un et indivisible, procédant du Verbe vrai et étant le Son originel, distingue deux méthodes essentielles :

**La partie « linguistique »**, qui consiste à prétraiter et transformer les informations en entrée en un jeu de données exploitable.

**La partie « apprentissage automatique »** ou « Data Science », qui porte sur l’application de modèles de Machine Learning ou Deep Learning à ce jeu de données.

.. figure:: ./Images/ortho.jpg
    :align: center

De manière très synthétique, on peut résumer l'utilisation de la bibliothèque NLTK en 4 grandes étapes : **préparation**, **extraction**, **analyse**, **prediction**.

Contraintes
-----------

NLTK fonctionne avec Python version 2 & 3

Technologies
------------
NLTK possède un ensemble de sous-packages et sous-modules pour la visualisation et l'intégration d'API (notamment des API en liens avec les réseaux sociaux).
Les dernières failles de sécurité répertoriées (et réparées) concernaient de possibles attaques ReDoS (Regular Expression Denial of Service).

Limites
--------

Une machine, aussi complexe soit-elle, n'est pas encore l'équivalent d'un être humain...

Par nature, le langage est ambigu. La machine, faute d’indices suffisamment saillants et de connaissances contextuelles, peut manquer l’interprétation juste. Il s’agit d’un problème vivace, malgré les progrès du machine learning et la présence de corpus de données toujours plus nombreux.

On parle de parasitisme computationnel, soit « la production d’analyses indésirables, inappropriées, résultant de l’application de règles tout à fait fondées linguistiquement par ailleurs » 
L’ambiguïté brouille depuis longtemps les cartes. Le problème est apparu d’une manière qui a marqué les esprits : lors de la première conférence internationale de traduction automatique, au MIT en 1962. Traduite en russe puis de nouveau en anglais, la phrase « The spirit is willing but the flesh is weak » est devenue ainsi « Vodka is strong but meat is rotten ». [#]_



.. [#] https://blog.clevy.io/conversationnel/introduction-au-nlp-5eme-partie/