# Lambda, calling itself into the lambda definition
&gt;&gt;&gt; import functools
&gt;&gt;&gt; f = lambda selflambda, x=x, *y: foo(x, y, selflambda)
&gt;&gt;&gt; f = functools.partial(f, f)
