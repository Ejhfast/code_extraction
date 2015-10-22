# Build dict applying expressions to an object
(lambda s: {"len" : len(s), "slice" : s[2:4]})(u'hello')
