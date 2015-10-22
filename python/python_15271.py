# How to convert hex string 'o\xf2\x00\x00' into a int32?
&gt;&gt;&gt; import struct
&gt;&gt;&gt; struct.unpack('&lt;i', 'o\xf2\x00\x00')
(62063,)
