# Elegant way to strip values in brackets in Python
&gt;&gt;&gt; Line = "A[0x04] Va   [0xf]"
&gt;&gt;&gt; [x.partition(']')[0] for x in Line.split('[') if ']' in x]
['0x04', '0xf']
