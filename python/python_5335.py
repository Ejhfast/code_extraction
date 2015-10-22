# How to escape dict from str in python?
&gt;&gt;&gt; ast.literal_eval('{"key1":"value1", "key2":"value2", "key3":"value3"}')
{'key3': 'value3', 'key2': 'value2', 'key1': 'value1'}
