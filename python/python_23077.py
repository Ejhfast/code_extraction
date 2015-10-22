# Issue when converting a tuple to a string
&gt;&gt;&gt; '\n'.join(' '.join(str(y) for y in x) for x in locations)
'John 32 21\nMichael 23 12'
