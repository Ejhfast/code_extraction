# Splitting a python dict from a certain key
n=3
d1 = {key: value for i, (key, value) in enumerate(d.items()) if i &lt; n}
d2 = {key: value for i, (key, value) in enumerate(d.items()) if i &gt;= n}
