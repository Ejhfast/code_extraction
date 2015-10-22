# List in the form of a string into a real list
import re
l = [int(i) for i in re.findall(r'(\d+)', "(1, 89, 67, 23)")]
print l
