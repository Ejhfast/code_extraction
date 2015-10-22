# list comprehension example for variable inner list
&gt;&gt;&gt; [x for x in l if all(y.strip() for y in x)]
[['200801', '100'], ['200802', '151'], ['200805', '160'], ['200812', '50']]
