# python regex to match whole line with a particular regex pattern
&gt;&gt;&gt; re.findall(r"(^.*?%s.*?$)" %expression, text, re.MULTILINE)
