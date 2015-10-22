# Concatenate certain letters in a string
&gt;&gt;&gt; ' '.join((' ' if pred else '').join(seq) for pred, seq in itertools.groupby("C S E majors in U S".split(), lambda x: len(x) &gt; 1))
'CSE majors in US'
