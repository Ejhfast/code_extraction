# what is the best way to unpack a FIX message into a python dictionary?
&gt;&gt;&gt; dict(p.split('=') for p in input.split('\001'))
{'key3': 'val3', 'key2': 'val2', 'key1': 'val1', 'key4': 'val4'}
