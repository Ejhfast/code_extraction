# sorted Dictionary to list
sorted(wordSimDic, key=lambda k: (wordSimDic.get(k), k), reverse=True)
