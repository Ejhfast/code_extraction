# Is there a python special character for a blank value?
def findit(word, lst):
    return [el[0] for el in lst if el[1] == word][0]
