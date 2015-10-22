# Parsing a string which represents a list of tuples
&gt;&gt;&gt; import ast
&gt;&gt;&gt; print ast.literal_eval("(8, 12.25), (13, 15), (16.75, 18.5)")
((8, 12.25), (13, 15), (16.75, 18.5))
