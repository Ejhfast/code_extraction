# Python: best way to find out from which set the results of `symmetric_difference` are from?
intersect = s1.symmetric_difference(s2)
result = dict([(i, ("s1" if i in s1 else "s2")) for i in intersect])
