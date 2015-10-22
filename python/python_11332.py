# Print a string as hex bytes?
&gt;&gt;&gt; s = "Hello world !!"
&gt;&gt;&gt; ":".join("{:02x}".format(ord(c)) for c in s)
'48:65:6c:6c:6f:20:77:6f:72:6c:64:20:21:21
