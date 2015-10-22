# Parse Java Source Files with Python
&gt;&gt;&gt; for m in re.finditer(r"\w+ly", text):
...     print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))
