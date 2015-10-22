# Split string and just get number in python?
&gt;&gt;&gt; text = "GoTo: 7018 6453 12654\n"
&gt;&gt;&gt; [token for token in text.split() if token.isdigit()]
['7018', '6453', '12654']
