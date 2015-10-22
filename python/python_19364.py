# Convert a byte array to string
&gt;&gt;&gt; s = "104,101,108,108,111"
&gt;&gt;&gt; "".join(chr(int(number)) for number in s.split(","))
'hello'
