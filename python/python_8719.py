# Python list appending while incrementing
&gt;&gt;&gt; strings = ["one two", "three four", "five six"]
&gt;&gt;&gt; [value for s in strings for value in s.split()]
['one', 'two', 'three', 'four', 'five', 'six']
