# tokenize a string keeping delimiters in Python
import re
splitter = re.compile(r'(\s+|\S+)')
splitter.findall(s)
