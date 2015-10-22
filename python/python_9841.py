# regular expression to match two digits numbers in a random string without matching 3 or more digit numbers
&gt;&gt;&gt; re.findall(r"(?&lt;!\d)\d\d(?!\d)", "abc123#d$45^abrt&amp;89*")
['45', '89']
