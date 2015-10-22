# Encoding issues (i think) when reading serial interface
p1_raw = ''.join(chr(ord(ch) &amp; 0x7f) for ch in p1_raw)
