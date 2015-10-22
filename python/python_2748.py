# Python list comprehension for dictionaries in dictionaries?
s = dict([ (k,r) for k,r in mydict.iteritems() if r['x'] &gt; 92 and r['x'] &lt; 95 and r['y'] &gt; 70 and r['y'] &lt; 75 ])
