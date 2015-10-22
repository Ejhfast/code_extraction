# In Python, how do I search a flat file for the closest match to a particular numeric value?
&gt;&gt;&gt; gen = (float(line.partition(' ')[0]) for line in open(fname))
&gt;&gt;&gt; min(enumerate(gen), key=lambda x: abs(x[1] - a))
(3, 2.453454)
