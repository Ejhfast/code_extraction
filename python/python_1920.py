# parsing words in string prefaced by 'password' with regex
&gt;&gt;&gt; re.findall(r"(?:password\sis\s+|password\:\s+)(\S+)", a)
['GOD', 'G0D']
