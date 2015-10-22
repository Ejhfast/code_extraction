# Python: split on two different expressions?
import re
re.split(r'&lt;(br\/|strong)&gt;wwww', mystr)[::2]
