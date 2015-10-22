# Python regular expression: find "com" or "org"
re.search('(com)|(org)',domain).span()[0]
