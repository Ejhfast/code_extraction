# Python regex reference conflicting with substitution number
import re
print re.sub(r'(\D+)(\d)$',r'\g&lt;1&gt;0\2','file1')
