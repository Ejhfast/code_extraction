# random byte string in python
&gt;&gt;&gt; import os
&gt;&gt;&gt; "\x00"+os.urandom(4)+"\x00"
'\x00!\xc0zK\x00'
