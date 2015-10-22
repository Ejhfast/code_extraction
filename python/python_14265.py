# Evaluating a function at a point in SymPy
&gt;&gt;&gt; vars = sorted(expression.free_symbols)
&gt;&gt;&gt; evaluated = expression.subs(*zip(vars, your_values))
