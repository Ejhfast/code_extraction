# count numbers associated with category in list
result = ""
for group in d:
    result += "%s, %s\n" % (group, sum(n for n in d[group]))
