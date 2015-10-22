# Get functions called in a Python expression
&gt;&gt;&gt; compile("cubic_fit(1, 2, get_data())", '&lt;string&gt;', 'eval').co_names
('cubic_fit', 'get_data')
