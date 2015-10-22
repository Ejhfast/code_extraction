# How do I capture words wrapped in parentheses with a regex in Python?
&gt;&gt;&gt; print re.search("(\w+) vs (\w+) \(\s?(\w+)",my_string).groups()
(u'Hibbert', u'Bosh', u'Chalmers')
