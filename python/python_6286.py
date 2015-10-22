# Key to maxima of dictionary in python
max_value = max(scores.values())
keys = [ i for (i,v) in scores.iteritems() if v == max_value ]
