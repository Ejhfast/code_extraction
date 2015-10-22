# String replace - avoid repeat
mapofcodes = {'USA': 'United States of America', ....}
for word in mystring.split():
    finalstr += mapofcodes.get(word, word)
