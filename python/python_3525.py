# Slice a binary number into groups of five digits
&gt;&gt;&gt; a='00010100011011101101110100010111'
&gt;&gt;&gt; [a[i:i+5] for i in range(0, len(a), 5)]
['00010', '10001', '10111', '01101', '11010', '00101', '11']
