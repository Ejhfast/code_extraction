# Python 3: How to convert a bytearray to an ASCII string
3&gt;&gt; bytearray(b'S\x00t\x00a\x00n\x00d\x00a\x00r\x00d\x00F\x00i\x00r\x00m\x00a\x00t\x00a\x00.\x00i\x00n\x00o\x00').decode('utf-16le')
'StandardFirmata.ino'
