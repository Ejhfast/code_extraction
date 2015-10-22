# Python easy way to set default encoding for opening files in text mode?
def utf8_open(*args, **kwargs):
    return open(*args, encoding='utf-8', **kwargs)
