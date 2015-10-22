# Building a list of months by iterating between two dates in a list (Python)
&gt;&gt;&gt; import itertools
&gt;&gt;&gt; [min(j) for i, j in itertools.groupby(A, key=lambda x: x[:7])]
['2001/01/01', '2001/02/04', '2001/03/01', '2001/04/10', '2001/05/07', '2001/07/01', '2002/03/01', '2002/04/01']
