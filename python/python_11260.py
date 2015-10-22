# bitwise rotating whole text
s = map(ord, text)
return ''.join(chr(((a&amp;1)&lt;&lt;7) + (b&gt;&gt;1)) for a,b in zip(s[-1:] + s, s))
