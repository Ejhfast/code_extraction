# convert dictionary entries into variables - python
&gt;&gt;&gt; d = {'a':1, 'b':2}
&gt;&gt;&gt; for key,val in d.items():
        exec(key + '=val')
