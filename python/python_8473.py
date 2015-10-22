# Absolute String matching in python
&gt;&gt;&gt; x = ["Albert Einstein", "test 1 s 2", "Einstein Albert", "foo bar baz", "baz foo bar"]
&gt;&gt;&gt; list(set(' '.join(sorted(s.split())) for s in x))
['bar baz foo', '1 2 s test', 'Albert Einstein']
