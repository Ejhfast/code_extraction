# Python: Inverse Replace Function
def inversereplace(text, word, repl):
    parts = text.split(word)
    return word.join(repl*len(x) for x in parts)
