# Trying to pack binary bits represented by bytes into a byte in python
3&gt;&gt; int('\x01\x01\x00\x01\x00\x01\x00\x01'.translate({0: '0', 1: '1'}), 2)
213
