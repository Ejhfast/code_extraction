# Join 3 tuples with string replacement
commands = tuple(prefix + ' ' + x.replace('&lt;PARAM&gt;',y) for x , z in zip(command,params) for y in z.split(','))
&gt;&gt;&gt; ('display command1 param 1 detail', 'display command1 param2 detail', 'display command1 param n detail', 'display command2 nextcom1 verbose', 'display command2 nextcom2 verbose', 'display command2 nectcom n verbose')
