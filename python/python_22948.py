# Remove every word of after a bracket and append remaining words to Python list
import re
s = "[AA BB, CC, DD, EE] [PP QQ, RR] [WW XX, YY, ZZ]"
response = re.findall('(?&lt;![[\w])\w+', s)
