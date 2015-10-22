# Detect English verb tenses using NLTK
len([phrase for phrase in nltk.Chunker(sentence) if phrase[1] == 'VP'])
