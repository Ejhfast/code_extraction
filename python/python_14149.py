# How to get all the hyponyms of a word/synset in python nltk and wordnet?
from nltk.corpus import wordnet as wn
vehicle = wn.synset('vehicle.n.01')
typesOfVehicles = list(set([w for s in vehicle.closure(lambda s:s.hyponyms()) for w in s.lemma_names]))
