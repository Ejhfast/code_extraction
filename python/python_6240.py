# Hex string to signed int in Python 3.2?
x = int(h,16)
if x &gt; 0x7FFFFFFF:
    x -= 0x100000000
