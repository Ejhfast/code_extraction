# Writing a 'print' function in Python
def log(*args):
    logging.info(' '.join(map(str, args)))
