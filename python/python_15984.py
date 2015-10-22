# Matching "..." = "..." in Python via Regex
&gt;&gt;&gt; matches = re.findall(r'"([^"]*)".=."([^"]*)"', line)
&gt;&gt;&gt; matches
[('string1', 'string2')]
