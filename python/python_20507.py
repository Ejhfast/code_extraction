# Reflection in Python: how to view all parameter of a function in Python 2.7
&gt;&gt;&gt; inspect.getargspec(a_function_somewhere)
ArgSpec(args=['arg1', 'arg2', 'arg3'],
        varargs=None, keywords=None, defaults=(None, 12))
