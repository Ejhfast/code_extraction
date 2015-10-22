# Inserting newline character after every 76 characters in a base64 string
'\n'.join(s[pos:pos+76] for pos in xrange(0, len(s), 76))
