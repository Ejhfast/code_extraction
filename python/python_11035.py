# escape utf8 decoding ('\x74' to 't')
&gt;&gt;&gt; s = "\x00\x12\xf8\x05\x74\xa2"
&gt;&gt;&gt; [ord(x) for x in list(s)]
[0, 18, 248, 5, 116, 162]
