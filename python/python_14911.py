# Comparing values from different tuples, list comprehension
[o for o,n in zip(old[0], new[0]) if float(o) &gt; float(n)]
