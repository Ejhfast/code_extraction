# Pyner empty dictionnary
&gt;&gt;&gt;import ner
&gt;&gt;&gt;tagger = ner.SocketNER(host='localhost', port=8081)
&gt;&gt;&gt;tagger.get_entities("University of California is located in California, United States")
