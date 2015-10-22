# Send formatted list of tuples as body of an email
body = '\n'.join('%s, %s' % pair for pair in mylist)
