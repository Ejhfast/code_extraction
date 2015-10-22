# Doing a bitwise operation on bytes
&gt;&gt;&gt; a, b = b'\x12', b'\x34'
&gt;&gt;&gt; bytes([a[0] &amp; b[0]])
b'\x10'
