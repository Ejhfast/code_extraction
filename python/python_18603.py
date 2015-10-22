# Python, concatenate each line of a file with one string
with open('palavras.txt', 'r+') as f:
    for lendo in f:
        print palavra + lendo,
