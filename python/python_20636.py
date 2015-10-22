# Split string into a list, with items of equal length
&gt;&gt;&gt; [string[start:start+4] for start in xrange(0, len(string), 4)]
['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx']
