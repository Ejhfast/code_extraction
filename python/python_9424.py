# Easily Alternate Delimiters in a Join
&gt;&gt;&gt; tuple = ('one', 'two', 'one', 'two', 'one')
&gt;&gt;&gt; ['&lt;strong&gt;%s&lt;/strong&gt;' % tuple[i] if i%2 else tuple[i] for i in range(len(tuple))]
['one', '&lt;strong&gt;two&lt;/strong&gt;', 'one', '&lt;strong&gt;two&lt;/strong&gt;', 'one']
