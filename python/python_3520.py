# how can I implement iteritems function for my custom iterator?
def iteritems(self):
    return iter([(x[0], x) for x in "alpha bravo charlie".split()])
