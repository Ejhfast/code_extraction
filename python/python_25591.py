# How to convert "\x1b" into a real control character "[Esc]"
s = r"1\x1b2"
dec = s.decode('string_escape')
print len(dec), repr(dec)
