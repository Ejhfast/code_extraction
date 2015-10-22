# autocomplete-like feature with a python dict
&gt;&gt;&gt; mydict={"fork" : True, "form" : True, "fold" : True, "fame" : True}
&gt;&gt;&gt; [k for k in mydict if k.startswith("for")]
['fork', 'form']
