# most efficient way to go about identifying sub-strings in a string in python?
&gt;&gt;&gt; cpv = re.compile(r'([0-9]+[-\. ]?[0-9])')
&gt;&gt;&gt; print cpv.findall('foo 30124120-1 bar 21966823.1 baz')
['30124120-1', '21966823.1']
