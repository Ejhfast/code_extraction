# What are the first 32 bits of the fractional part of this float?
&gt;&gt;&gt; hex(int(math.modf(math.sqrt(2))[0]*(1&lt;&lt;32)))
'0x6a09e667'
