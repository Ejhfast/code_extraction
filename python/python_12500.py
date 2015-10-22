# Change the value of a dictionary to key of a dictionary in python
def reverseTranslation(d):
    return dict((v1,[k for k,v in d.iteritems() if v1 in v])
                for v1 in set(sum(d.values(),[])))
