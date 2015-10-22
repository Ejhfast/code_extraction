# Python: Combine "if 'x' in dict" and "for i in dict['x']"
for x in d.get("kids", ()):
    print "kid:", x
