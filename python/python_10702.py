# Python function for capping a string to a maximum length
def cap(s, l):
    return s if len(s)&lt;=l else s[0:l-3]+'...'
