# python regex find line1 and value after line 1, find line2 and value after line2...etc
&gt;&gt;&gt; import re
&gt;&gt;&gt; regex  = re.compile(r'(?s)name:\s*\((\w+)\).*?year:\s*\((\w+)\)')
&gt;&gt;&gt; mydict = dict(re.findall(regex, data))
