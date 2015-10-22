# Comparing two dictionaries in Python
shared_items = set(x.items()) &amp; set(y.items())
print len(shared_items)
