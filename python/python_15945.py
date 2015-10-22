# Single quote replacement, handling of null integers in pandas/python2.7
In [144]: list([ "{%s , %s}" % tup[1:] for tup in df.replace(np.nan,0).astype(int).replace(0,'').itertuples() ])
Out[144]: ['{1 , 4}', '{2 , 3}', '{3 , }', '{4 , 1}']
