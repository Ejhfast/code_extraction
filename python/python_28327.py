# How to specify string variables as unicode strings for pattern and text in regex matching?
re.match(myregex.decode('utf-8'), mytext.decode('utf-8'))
