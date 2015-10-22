# Optimize double enumerate loops
for v in data.itervalues():
  v['events'][:] = [e for e in v['events'] if e['displayed']]
