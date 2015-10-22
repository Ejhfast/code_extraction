# I'm looking for a pythonic way to insert a space before capital letters
&gt;&gt;&gt; re.sub(r"(\w)([A-Z])", r"\1 \2", "WordWordWord")
'Word Word Word'
