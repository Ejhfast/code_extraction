# Removing specific html tags with python
import re
s = '&lt;table style="width: 100%%" bgcolor="%s"&gt;&lt;tr&gt;&lt;td&gt;&lt;font color="%s"&gt;&lt;b&gt;1.23&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;'
result = float(re.sub(r"&lt;.?table[^&gt;]*&gt;|&lt;.?t[rd]&gt;|&lt;font[^&gt;]+&gt;|&lt;.?b&gt;", "", s))
