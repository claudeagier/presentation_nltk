Comment ça marche
=================

Pré-requis
----------
Avoir python d'installer 
Python versions 3.7, 3.8, 3.9 or 3.10

Installation
------------

Installation du package
::
    pip install --user -U nltk


Installation des models et des datasets prédéfinis
::
    en ligne de commande
    python -m nltk.downloader popular

    ou dans un notebook
    nltk.download('popular')

.. figure:: ./Images/nltk_ide.png

Usage
------

::
    import nltk

    #où l'une de ses méthodes 

    from nltk.stem.snowball import SnowballStemmer
    from nltk.probability import FreqDist
    from nltk.tokenize import word_tokenize

nltk possède aussi un corpus de textes très fourni pour aiguiser ses armes
::
    from nltk.corpus import hamlet

Principes
---------

- Pré-traitement : une étape qui cherche à standardiser du texte afin de rendre son usage plus facile
- Représentation du texte comme un vecteur : Cette étape peut être effectuée via des techniques de sac de mots (Bag of Words) ou Term Frequency-Inverse Document Frequency (Tf-IdF). On peut également apprendre des représentations vectorielles (embedding) par apprentissage profond.
- Classification, trouver la phrase la plus similaire… (optionnel)


.. figure:: ./Images/schema.png


Méthode
-------
 comment utilisez cette bibliothèque de façon orthodoxe

Contraintes
-----------
en termes de sécurité, de version, d'environnement technologique, …
	version python pep 8

Technologies
------------
 / langage employées en plus du Python (le cas échéant) : 
HTML/CSS/Javascript/SQL/…


