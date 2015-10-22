# How do i get 10 random values in python?
&gt;&gt;&gt; from random import randint as r
&gt;&gt;&gt; array = [ (r(1,100), r(1,100)) for i in xrange(10)]
