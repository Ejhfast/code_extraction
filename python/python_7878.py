# For every string get unique combination of 3 chars (together)
&gt;&gt;&gt; s = "combination.py"
&gt;&gt;&gt; [s[i:i+3] for i in range(len(s)-2)]
['com', 'omb', 'mbi', 'bin', 'ina', 'nat', 'ati', 'tio', 'ion', 'on.', 'n.p', '.py']
