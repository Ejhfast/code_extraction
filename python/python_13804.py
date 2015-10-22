# Creating packet using struct.pack with python
&gt;&gt;&gt; struct.pack('!L4sL4s', field1, socket.inet_aton(field2),
                           field3, socket.inet_aton(field4))
'\x00\x00\x00\x01\xff\xff\xff\x00\x00\x00\x00\x14\xc0\xa8\x00\x01'
