# smartest way to join two lists into a formatted string
c = ', '.join('%s=%s' % t for t in zip(a, b))
