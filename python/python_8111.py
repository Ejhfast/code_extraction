# How does len function actually work for files?
&gt;&gt;&gt; open("file.txt", 'w').write("one two three")
&gt;&gt;&gt; len(open("file.txt").read())
13
