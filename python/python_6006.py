# In list of dicts, match dict based on one key/value?
fields = ('name', 'school')
match_found = any(all(x[f]==example[f] for f in fields) for x in myList)
