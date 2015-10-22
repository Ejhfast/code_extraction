# locals().update(dictionary) doesn't add all the variables
def func():
    locals()['val'] = 1
    print val
