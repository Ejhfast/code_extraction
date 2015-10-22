# How to pass arguments to function of callable-iterator in python?
&gt;&gt;&gt; call_iter = iter(lambda:lambda x: x + 1, 100)
&gt;&gt;&gt; next(call_iter)(1)
2
