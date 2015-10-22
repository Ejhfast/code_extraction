# How to build a short out of char(s) in Python using bit shift?
lower = ctypes.cschar(&lt;somevalue&gt;)
upper = ctypes.cschar(&lt;anothervalue&gt;)
combined = ctypes.csshort( lower + (upper &lt;&lt; 8) )
