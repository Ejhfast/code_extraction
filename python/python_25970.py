# Python: Grab each word after certain character in string
&gt;&gt;&gt; my_str = "word anotherword +aspecialword lameword +heythisone +test hello"
&gt;&gt;&gt; " ".join(x[1:] for x in my_str.split() if x.startswith("+"))
'aspecialword heythisone test'
