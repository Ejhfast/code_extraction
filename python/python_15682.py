# Split at multiple delimiter without delimiter in the list
&gt;&gt;&gt; re.split(r'\[|\]', data2)
['A new string. ', 'with brackets', ' another line ', 'and a bracket', '']
