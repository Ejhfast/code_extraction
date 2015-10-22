# Excluding captured group in re.split
&gt;&gt;&gt; re.split(r'\n(?=[A-Z]{2,3},)', contents)
['US,This\nis the title', 'CA, New Title', 'CA, Newer Title']
