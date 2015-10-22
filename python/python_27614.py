# Convert binary string to hex string and keep its leading zeros
&gt;&gt;&gt; bits = "0000000000001010"
&gt;&gt;&gt; '{:0{}X}'.format(int(bits, 2), len(bits) // 4)
'000A'
