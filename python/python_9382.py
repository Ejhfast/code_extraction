# python struct module - odd values when unpacking
&gt;&gt;&gt; con = b'\x00\x00\x00\x01'
&gt;&gt;&gt; struct.unpack('&gt;i', con)
(1,)
