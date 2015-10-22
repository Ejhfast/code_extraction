# Regex query on not operator
s = '\\x20\\x20\\x20asdasd\\x20\\x20\\x20asd\\x20a12v\\x20123123\\x20\\x20'
s = s.decode('string-escape')
s = ''.join('\\x%2x' % ord(c) for c in s)
