# Python - Iterating through a list of list with a specifically formatted output; file output
for j in data:
    text_file.write('%s\n' % '\t'.join(str(x) for x in j))
