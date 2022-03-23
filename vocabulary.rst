Un peu de Vocabulaire
=====================

Tokenization
------------
découpage du texte en token, le token étant une unité sémantique avec un sens.

Stop-word
---------
les mots qui n'apportent pas de sens au texte, les articles, les pronoms

Stemming
--------
Un même mot peut se retrouver sous différentes formes en fonction du genre (masculin féminin), du nombre (singulier, pluriel), la personne (moi, toi, eux…) etc. Le stemming désigne généralement le processus qui consiste à découper la fin des mots afin de ne conserver que la racine du mot.

lemmatization
-------------
Cela consiste à réaliser la même tâche mais en utilisant un vocabulaire et une analyse fine de la construction des mots. La lemmatisation permet donc de supprimer uniquement les terminaisons inflexibles et donc à isoler la forme canonique du mot, connue sous le nom de lemme.

Term-Frequency (TF)
-------------------

cette méthode consiste à compter le nombre d’occurrences des tokens présents dans le corpus pour chaque texte. Chaque texte est alors représenté par un vecteur d’occurrences. On parle généralement de Bag-Of-Word, ou sac de mots en français.

.. NOTE::

    Néanmoins, cette approche présente un inconvénient majeur : certains mots sont par nature plus utilisés que d’autres, ce qui peut conduire le modèle à des résultats erronés.

Term Frequency-Inverse Document Frequency (TF-IDF)
--------------------------------------------------
cette méthode consiste à compter le nombre d’occurrences des tokens présents dans le corpus pour chaque texte, que l’on divise ensuite par le nombre d’occurrences total de ces même tokens dans tout le corpus.

.. WARNING::

    Plus le vocabulaire du corpus est riche, plus la taille des vecteurs est grande, ce qui peut représenter un problème pour les modèles d’apprentissage.
    Le comptage d’occurrence des mots ne permet pas de rendre compte de leur agencement et donc du sens des phrases.
