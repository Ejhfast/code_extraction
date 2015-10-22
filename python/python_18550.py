# Pythonic way of converting a list embedded in a string to a list
&gt;&gt;&gt; import ast
&gt;&gt;&gt; ast.literal_eval('[1,2,3]')
[1, 2, 3]
