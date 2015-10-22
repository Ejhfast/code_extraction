# Many Repeated Tuples in list
for index, (word,tag) in enumerate(simpleTag):
    if word.startswith('samsung'):
        simpleTag[index] = (word, 'NOUN')
