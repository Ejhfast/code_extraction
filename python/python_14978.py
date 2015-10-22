# check if item is in list and then return the item
&gt;&gt;&gt; input = ['a;1,2,3\n', 'b;abc\n']
&gt;&gt;&gt; filter(lambda item:item.find('b;') == 0 ,input)
['b;abc\n']
