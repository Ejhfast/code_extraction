# How can I insert text at every number in a string
import re
print re.sub(r'(\d+)','{\sub \\1}','C5B2GH5')
#output: C{\sub 5}B{\sub 2}GH{\sub 5}
