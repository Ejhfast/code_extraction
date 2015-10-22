# How to format string width with a runtime calculated variable?
&gt;&gt;&gt; width = 40
&gt;&gt;&gt; '{0:&lt;{width}}'.format('aa', width=width)
'aa                                      '
