# How to get a value and its key from a dictionary
&gt;&gt;&gt; d = {'0003': ['Mike', 'Restrepo', 'mtrepot', '87654321'], '0001': ['John', 'Jelenski', 'jelensohn', 'snf23jn4'], '0002': ['Clyde', 'Owen', 'clonew', 'dummy2015']}
&gt;&gt;&gt; [k for k, v in d.items() if 'mtrepot' in v]
['0003']
