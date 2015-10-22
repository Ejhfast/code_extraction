# Python3 ASCII Hexadecimal to Binary String Conversion
3&gt;&gt; ''.join(chr(int(x, 16)) for x in "0x000A 0x000B 0x000C 0x000D".split()).encode('utf-16be')
b'\x00\n\x00\x0b\x00\x0c\x00\r'
