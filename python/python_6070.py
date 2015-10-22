# Multiple splits on a single line in Python
import re
regex = re.compile(r'[,:/]')
a, b, c, d, e = regex.split('a,b:c,d/e')
