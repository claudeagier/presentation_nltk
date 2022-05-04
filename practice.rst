
.. role:: text-bold

NLTK dans la pratique
=====================

    .. figure:: ./Images/idea.png
        :align: center

Démonstration
-------------

Analyse de tweets sur le thème de l'élection présidentielle.
Pour cette démonstration, nous verrons comment utiliser NLTK pour analyser des données textuelles en français.
Cette bibliothèque n'est pas très adaptée à la langue française : il faut donc faire quelques recherches pour pouvoir utiliser correctement cette librairie en français.

La première étape de cette démonstration a été de récupérer des tweets via l'API Twitter.
Le dataset est constitué d'environ 600 tweets anonymisés.

Import des bibliothèques
~~~~~~~~~~~~~~~~~~~~~~~~

:text-bold:`Installation des packages`
::
    import nltk
    from nltk.corpus import stopwords

    # fonctions, classes et méthodes pour l'analyse du français
    from nltk import RegexpTokenizer
    from nltk.stem.snowball import FrenchStemmer

    # from nltk.tokenize import sent_tokenize
    from nltk.probability import FreqDist
    import re
    import pandas as pd

Chargement du fichier json
~~~~~~~~~~~~~~~~~~~~~~~~~~

:text-bold:`Création du dataframe`
::
    tweets = pd.read_json("test_tweets.json", orient="records", encoding='utf-8')
    tweets.head()
    tweets = tweets.astype(str)
    print(tweets.info())

Mise en place des filtres à utiliser pour préparer les données
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:text-bold:`Chargement du dictionnaire de stop-words`
::
    # dictionnaire de mots stop en francais
    french_stopwords = set(stopwords.words('french'))

    # add stop-words
    french_stopwords.add('cette')
    french_stopwords.add('où')

:text-bold:`Fonction de filtrage des mots`
::
    # filtrer tous les caractères spéciaux
    regexp = re.compile(r"""[\.\!\"\s\?\-\,\'\_\@\…\/\#\:\’]+""")

    def avoid(word):
        return regexp.search(word) or word == "https"

    #filtrer les stop-words
    filtre_stopfr =  lambda text: [token for token in text if token.lower() not in french_stopwords]

Instanciation des utilitaires français
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:text-bold:`Instanciation du tokenizer`

Il est recommandé de faire un tokenizer custom avec une regexp pour gérer au mieux le tronçonnage des phrases en mots.
::
    # french tokenizer
    # from nltk import RegexpTokenizer
    toknizer = RegexpTokenizer(r'''\w'|\w+|[^\w\s]''')

:text-bold:`Instanciation de stemmer`

Il faut utiliser une classe spécifique à la langue française pour la recherche du radical du mot. Il existe différents stemmers pour chaque langue.
::
    # french stemmer
    # from nltk.stem.snowball import FrenchStemmer
    fs = FrenchStemmer()


:text-bold:`Instancier c'est bien, s'en servir c'est mieux`

Pour ce faire, je crée quelques fonctions.
::
    # tokenization de tous les mots 
    def get_text_tokenized(text):
        tokens = toknizer.tokenize(text)
        return filtre_stopfr(tokens)

    # stemmatisation des mots (racine)
    def get_stem(tokenized_text):
        return [fs.stem(tokens) for tokens in tokenized_text if not avoid(tokens)]

    # Contient des caractères spéciaux ?
    regexp = re.compile(r"""[\.\!\"\s\?\-\,\'\_\@\…\/\#\:\’]+""")

    def avoid(word):
        return regexp.search(word) or word == "https"


Analyse des tweets
~~~~~~~~~~~~~~~~~~
:text-bold:`Fréquence de distribution des mots et top 7`

**Question : Afficher les 7 mots les plus cités**
::
    fd = FreqDist()

    for tweet in tweets['text']:
        ....

    
    fdist_top7 = fd.most_common(7)
    fdist_top7
# indices : loop inception

Output
::
   [
       ('présidentielle', 323),
       ('macron', 160),
       ('co', 135),
       ('élection', 127),
       ('zemmour', 79),
       ('campagne', 79),
       ('emmanuel', 75)
    ]

**Réponse**
::
    fd = FreqDist()

    for tweet in tweets['text']:
        #frequence distribution
        for word in get_text_tokenized(tweet):
            if not avoid(word):
                fd[word.lower()]+=1  
            
    # for key, value in  enumerate(fd):
    #     print(f"{key} : {value}")

    fdist_top7 = fd.most_common(7)
    fdist_top7


        
**Résultat**
::
   [
       ('présidentielle', 323),
       ('macron', 160),
       ('co', 135),
       ('élection', 127),
       ('zemmour', 79),
       ('campagne', 79),
       ('emmanuel', 75)
    ]

Installation d'un tagger pour la langue française
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:text-bold:`Installation tagger pour la langue française`

Après quelques recherches sur les internets, le meilleur tagger pour la langue française est un module Java, développé par Stanford.
Il semble que le plus sûr moyen d'arriver à nos fins est de suivre la doc d'installation suivante:
"http://www.linguisticsweb.org/doku.php?id=linguisticsweb:tutorials:automaticannotation:stanford_pos_tagger"

Il faut donc utiliser un module Java dans notre code Python (oui, on peut) :
 - installer jdk 8
 - téléchager le .jar  Stanford Tagger version 4.2.x 
 - dézipper
 - copier le répertoire dézippé dans "C:/Users/Public/utility/"

Ensuite dans le code :
::
    from nltk.tag.stanford import StanfordPOSTagger
    import os

    # enter the path to your local Java JDK, under Windows, the path should look very similar to this example
    java_path = "C:/Program Files/Java/jdk-18/bin/java.exe"
    os.environ["JAVAHOME"] = java_path
    
    # enter the paths to the Stanford POS Tagger .jar file as well as to the model to be used
    jar = "C:/Users/Public/utility/stanford-tagger-4.2.0/stanford-postagger-full-2020-11-17/stanford-postagger.jar"
    model = "C:/Users/Public/utility/stanford-tagger-4.2.0/stanford-postagger-full-2020-11-17/models/french-ud.tagger"
    
    # instanciation
    pos_tagger = StanfordPOSTagger(model, jar, encoding = "utf-8")

:text-bold:`Utilisation du tagger pour définir la nature des mots`

La liste des tags est ici : https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/
::
    # Récupération des noms propres
    all_names = set()
    for tweet in tweets['text']:
        all_tags = pos_tagger.tag(get_text_tokenized(tweet))
        [all_names.add(tag[0]) for tag in all_tags if tag[1] == "NOUN"]
    print(all_names)

Output
::
    {
        'retransmis',
        'ménages', 
        'entourage', 
        'gagnante', 
        'débat',
        ...
        'président', 
        'appel', 
        'retraite', 
        'Français', 
        'règles'
    }
