# Clearing all elements from all arbitrary lists of sublists in python
def clearsublists(L):
    return [clearsublists(l) for l in L if isinstance(l, list)]
