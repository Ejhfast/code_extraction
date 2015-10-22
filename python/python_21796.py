# get the index of the string elements which are common to more than one lists
_all = list(set(A))+list(set(B))+list(set(C))
indexes = [[u.index(x) for x in u if (_all).count(x) &gt; 1] for u in [A, B, C]]
