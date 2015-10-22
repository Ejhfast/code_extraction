# Convert dictionary to a string and separate by coma each key-value pair
&gt;&gt;&gt; ", ".join(["=".join([key, str(val)]) for key, val in data.items()])
'foo=1, bar=2'
