# python: complicated loop through list
needed = set(['ALGIDON','ALGOLYSIN','AMIDON','DEPRIDOL','DOLOPHINE','FENADONE', 'METHADOSE','MIADONE','PHENADONE'])
b = filter(lambda s: len(set(s.upper().split(',')) &amp; needed) &gt; 0, b)
