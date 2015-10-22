# Using .find to search a string inside a list
&gt;&gt;&gt; list_of_strings = ['Hello!, my name is Carl', 'Hello!, my name is Steve', 'Hello!, my name is Betty', 'My Name is Josh']
&gt;&gt;&gt; [s.find('Hello!') for s in list_of_strings]
[0, 0, 0, -1]
