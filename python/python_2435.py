# How to make "int" parse blank strings?
def mk_int(s):
    s = s.strip()
    return int(s) if s else 0
