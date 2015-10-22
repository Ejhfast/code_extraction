# subtract a string from another string
import string
def getAvailableLetters(lettersGuessed):
    return set(string.ascii_lowercase) - set(lettersGuessed.lower())
