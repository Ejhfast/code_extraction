# Find first x matches with re.findall
&gt;&gt;&gt; import itertools as IT
&gt;&gt;&gt; [item.group() for item in IT.islice(re.finditer(r'\d', text), 3)]
['1', '2', '3']
