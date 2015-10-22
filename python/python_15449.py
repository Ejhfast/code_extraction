# Python: Find Surrounding parts of a string with irrelevant section in the middle
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.findall(r'blah"(\d+)"','"0" blah"11" "0" blah"3" "0" blah"6" "0" blah"600" "0"')
['11', '3', '6', '600']
