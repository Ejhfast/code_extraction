# Keep strings that occur N times or more
[s for s, c in counts.iteritems() if c &gt;= 2]
# =&gt; ['a', 'c', 'b']
