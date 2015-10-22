# How to escape os.system() calls in Python?
def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"
