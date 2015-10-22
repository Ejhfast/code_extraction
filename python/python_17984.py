# Extracting strings in Python in either single or double quotes
&gt;&gt;&gt; buffer="tags = { 'one' : \"two\", \"three\", 'four' }"
&gt;&gt;&gt; re.findall(r"['\"](.*?)['\"]", buffer)
['one', 'two', 'three', 'four']
