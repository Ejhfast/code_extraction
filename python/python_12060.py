# Reversible hash function?
def hash(n):
  return ((0x0000FFFF &amp; n)&lt;&lt;16) + ((0xFFFF0000 &amp; n)&gt;&gt;16)
