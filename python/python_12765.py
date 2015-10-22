# Reading substrings from string in Python
import re
print dict(re.findall('TEXTSTART\[([^\]]+)\](.*?)TEXTEND', report, re.DOTALL))
