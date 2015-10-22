# Inverting Dictionaries in Python
import operator
inverted = dict((v,k) for k,v in sorted(d.iteritems(), key=operator.itemgetter(1)))
