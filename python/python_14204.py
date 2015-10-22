# How to get the princeton WN sense id given a sense offset? Python-NLTK
&gt;&gt;&gt; senseIdToSynset = {s.offset:s for s in wn.all_synsets()}
&gt;&gt;&gt; senseIdToSynset[2084071]
Synset('dog.n.01')
