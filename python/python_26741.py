# How to delete multiple substrings in Python?
import re
re.sub(r'\s*{.*?}\s*', ' ', my_string)
# '1.e4 c5 2.Nf3 d6 3.d4 Nxd4 '
