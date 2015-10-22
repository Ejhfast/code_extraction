# How to enumerate combined strings as the search range of for..in loop?
for filename in ("%smanifest-%s.txt" % (prefix, a)
    for prefix in ['', 'tag'] for a in checksum_algos):
