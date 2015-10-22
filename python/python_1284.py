# Munging non-printable characters to dots using string.translate()
filter = ''.join([['.', chr(x)][chr(x) in string.printable[:-5]] for x in xrange(256)])
