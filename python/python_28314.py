# TypeError: 'generator' object has no attribute '__getitem__'
rows_generator = genSearch(SearchInfo)
row2 = next(rows_generator, None)
print row2['SearchDate']
