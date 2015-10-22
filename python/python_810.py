# How do we remove all non-numeric characters from a string in Python?
&gt;&gt;&gt; import re
&gt;&gt;&gt; re.sub("[^0-9]", "", "sdkjh987978asd098as0980a98sd")
'987978098098098'
