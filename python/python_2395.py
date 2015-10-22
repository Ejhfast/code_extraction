# python: multiline regular expression
re.findall(r'Hello, (?P&lt;login&gt;[^.]+)\..+?hash: (?P&lt;hash&gt;[^.]+)', test_str, re.S)
