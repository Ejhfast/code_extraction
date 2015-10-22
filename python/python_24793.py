# Python: remove item from list if item has a number
&gt;&gt;&gt; [ item for item in lst if not any(char.isdigit() for char in item) ]
['unfavorable movements in foreign exchange rates', 'institutions to protect against foreign exchange risks']
&gt;&gt;&gt;
