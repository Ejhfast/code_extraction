# How to sort a dict by values and return a list of formatted strings?
result = ['{1} - {0}'.format(*pair) for pair in sorted(text_to_count.iteritems(), key = lambda (_,v): v, reverse = True)]
