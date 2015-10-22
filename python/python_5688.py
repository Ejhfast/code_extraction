# Using regular expressions to modify a string
&gt;&gt;&gt; re.sub("([0-9]+:[0-9]+)", "\\1.0", ':: 1:62 2:31 :: 3:4 4:32')
':: 1:62.0 2:31.0 :: 3:4.0 4:32.0'
