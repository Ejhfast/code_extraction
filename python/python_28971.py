# How to parse a large malformed HTML page, in Python?
import re
trs = re.findall(r'(?&lt;=&lt;tr&gt;).*?(?=&lt;tr&gt;)', your_string, re.DOTALL)
print trs
