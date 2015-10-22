# Split UTF-8 encoded string got from unichr
&gt;&gt;&gt; [hex(ord(x)) for x in unichr(0x80).encode('utf-8')]
['0xc2', '0x80']
