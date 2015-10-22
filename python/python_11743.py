# How do I extract some string from a long string in Python?
import re
results = re.findall(r'\bhttp://www\.someDomainName\.com/\d+\b', long_string)
