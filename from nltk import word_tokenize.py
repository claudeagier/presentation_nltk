words= 'words'

from nltk.stem.porter import PorterStemmer

stemmed = [PorterStemmer().stem(w) for w in words]