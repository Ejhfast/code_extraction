# Comparison of arrays and calculation
for newr in new_r:
  print [(r[i+1]-r[i])**3 * ro[i+1] for i in xrange(len(r) - 1) if r[i] &lt; newr]
