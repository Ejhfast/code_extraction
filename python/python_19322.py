# Writing bits to a binary file
&gt;&gt;&gt; bits = "10111111111111111011110"
&gt;&gt;&gt; int(bits[::-1], 2).to_bytes(4, 'little')
b'\xfd\xff=\x00'
