# Remove ASCII control characters from text file Python
&gt;&gt;&gt; import string
&gt;&gt;&gt; filter(string.printable.__contains__, '\x00\x01XYZ\x00\x10')
'XYZ'
