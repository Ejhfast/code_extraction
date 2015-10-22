# Parse out key:values in dictionary nested in MRSS feed using Python Feedparser
for key, val in item.media_content[0].iteritems():
    print key, val
