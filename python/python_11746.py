# Removing an item from list matching a substring - Python
&gt;&gt;&gt; [x for x in sents if not x.startswith('@$\t') and not x.startswith('#')]
['this doesnt', 'this shouldnt', 'this isnt', 'this musnt']
