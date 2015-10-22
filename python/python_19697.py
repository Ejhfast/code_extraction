# Splitting a string with brackets using regular expression in python
data = "[Hi all], [this is] [an example] "
import re
print re.findall("\[(.*?)\]", data)    # ['Hi all', 'this is', 'an example']
