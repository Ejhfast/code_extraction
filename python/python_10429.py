# Way to extract several substrings from a string?
q = "today(Thursday)^05^*07*[2012]"
import re
print re.findall(r'\w+', q) # ['today', 'Thursday', '05', '07', '2012']
