# Split line by +-*/() (as delimeters) without omitting them in python
&gt;&gt;&gt; re.findall(r'\d+|[-+/*()]', infix)
['(', '22', '+', '33', ')', '*', '44', '/', '300']
