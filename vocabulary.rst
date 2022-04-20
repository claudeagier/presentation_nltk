Un peu de Vocabulaire linguistique :
=====================================


.. role:: text-bold
.. figure:: ./Images/voc.jpg 
    :align: center 

.. NOTE::
    Nous allons bien sûr rester ici dans le domaine du vocabulaire propre à la bibliothèque et ne pas nous attarder sur des notions de linguistique qui s'avéreraient par trop complexes.

Langage
-------
Au sens large, le langage se définit comme un système de signes qui associe des mots selon des règles grammaticales précises, il renvoie à la faculté de raisonner, de nommer les choses et de communiquer avec autrui.

.. NOTE::
    Au passage, ceci est un mythe, merci de l'oublier pour de bon.
   
   
.. figure:: ./Images/wrong.png

Sens
----
En linguistique, est la signification d'une expression (mot, syntagme, phrase, énoncé, etc.), c'est-à-dire l'idée qui y est associée, dite aussi dénotation, avec ou sans connotations. Les interrogations au sujet de ce que constitue la signification, ou le sens, sont à la base de la philosophie du langage.

Analyse sémantique
------------------
L’analyse sémantique consiste ainsi à établir la signification d’une phrase en utilisant le sens des éléments la composant. Dans la NLP, elle s'appuie sur les éléments suivants :

- :text-bold:`l’approche linguistique`, avec l'établissement a priori des règles en étudiant le langage
- :text-bold:`l’approche statistique`, avec pour base l’analyse de corpus importants, à partir desquels la machine va extraire des règles grâce à l’apprentissage automatique (machine learning);
- :text-bold:`les approches hybrides`, situées entre linguistique et statistique qui permettent d’obtenir de meilleurs résultats.

Analyse lexicale
----------------
L'analyse lexicale est fondée sur la statistique fréquentielle, c'est-à-dire la redondante des traces lexicales et les proximités entre les mots.

Un peu de Vocabulaire NLP :
===========================

Tokenization
------------
Il s'agit de découper le texte en "tokens", le token étant une unité sémantique individuelle avec un sens grammatical. En tokenizant, si un mot apparaît plusieurs fois dans le texte, il sera compté plusieurs fois.

Stop-word
---------
Ce sont les mots qui sont généralement filtrés avant de traiter un langage. Ils regroupent les mots les plus communs d'un langage (articles, prépositions, pronoms, conjonctions, etc.) qui n'apportent pas beaucoup d'information quant au sens du texte.

Stemming
--------
Un même mot peut se retrouver sous différentes formes en fonction du genre (masculin féminin), du nombre (singulier, pluriel), de la personne (moi, toi, eux…) etc. Le stemming désigne généralement le processus qui consiste à découper la fin des mots afin de ne conserver que la racine du mot.

Lemmatisation
-------------
Cela consiste à réaliser la même tâche mais en utilisant une analyse et un vocabulaire fins de la construction des mots. La lemmatisation permet donc de supprimer uniquement les terminaisons inflexibles et donc à isoler la forme canonique du mot, connue sous le nom de lemme.

Term-Frequency (TF)
-------------------

Cette méthode consiste à compter le nombre d’occurrences de mots présents dans le corpus pour chaque texte. Chaque texte est alors représenté par un vecteur d’occurrences. On parle généralement de Bag-Of-Word, ou sac de mots en français.

.. NOTE::

    Cette approche présente un inconvénient majeur : certains mots sont par nature plus utilisés que d’autres, ce qui peut conduire le modèle à des résultats erronés.

Term Frequency-Inverse Document Frequency (TF-IDF)
--------------------------------------------------
Cette méthode consiste à compter le nombre d’occurrences de mots présents dans le corpus pour chaque texte, que l’on divise ensuite par le nombre d’occurrences total de ces mêmes mots dans tout le corpus.


P.O.S. : Parts Of Speech / Tagging
----------------------------------
Cette méthode consiste à analyser la nature sémantique des mots d'un texte : noms, pronoms, adjectifs, verbes, adverbes, conjonctions etc. Il existe plus de 36 catégories de mots (NN pour nom, NNP pour nom propre, DET pour déterminant, etc.).

Chunking
---------
Chunk = morceau. Rassembler des éléments de langages individuels en plus gros groupes (verbaux, nominaux, compléments divers etc.).

N.E.R. : Name Entity Recognition 
--------------------------------

Vient en complémentarité de la tokenization d'une texte pour identifier des catégories de noms : entreprises, locations, géopolitiques, organisations, personnes, géo-sociologiques). Se fait également à l'aide de la méthode de chunking.

Parsing
--------
Méthode utilisée pour passer en revue tous les éléments d'un texte afin d'en dégager une arborescence. Bien qu'il puisse être utilisé pour identifier les différents éléments d'un texte, le parsing peut aussi servir à analyser les morphèmes (soit les composantes morphologiques d'un mot).

Arbre syntaxique
-----------------
Il représente la structure syntaxique d'une phrase. Dans la bibliothèque NLTK, l'arbre donne une représentation visuelle de l'organisation syntaxique de la phrase, basée sur le travail de tagging . Chaque rameau est relié à une branche par un "node" (nœud), elle-même reliée au tronc qui représente la phrase dans son ensemble.

.. figure:: ./Images/syntax_tree.png


.. WARNING::

    Plus le vocabulaire du corpus est riche, plus la taille des vecteurs est grande, ce qui peut représenter un problème pour les modèles d’apprentissage.
    Le comptage d’occurrences de mots ne permet pas de rendre compte de leur agencement et donc du sens des phrases.

