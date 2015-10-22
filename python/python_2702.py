# Python converting the values from dicts into a tuples
&gt;&gt;&gt; l = [{'id':1,'name':'Foo'},{'id':2,'name':'Bar'}]
&gt;&gt;&gt; [tuple(d.values()) for d in l]
[(1, 'Foo'), (2, 'Bar')]
