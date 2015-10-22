# I'm trying to understand how I can search for three different types of strings
regex = re.compile( "(%s|%s|%s)" % ( re.escape( userstring ), re.escape( userStrHEX ), re.escape( userStrASCII ) )
