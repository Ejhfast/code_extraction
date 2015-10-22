# How can I determine the byte length of a utf-8 encoded string in Python?
def utf8len(s):
    return len(s.encode('utf-8'))
