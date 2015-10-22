# How to find if a secret word contains all the characters from a list?
def isWordGuessed(secretWord, lettersGuessed):
    return set(secretWord) &lt;= set(lettersGuessed)
