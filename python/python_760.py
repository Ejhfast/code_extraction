# Using a caesarian cipher on a string of text in python?
def encode(s):
    l = [ord(i) for i in s]
    return ''.join([chr(i + 2) for i in l])
