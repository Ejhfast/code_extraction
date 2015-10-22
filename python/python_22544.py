# convert unicode into list
lframe = [x for x in [e.encode('utf-8') for e in frame.split(',')][0]]
