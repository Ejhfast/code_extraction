# Regex for multi character strings embedded in rest of match?
import re
re.search('(AB|CD|EF)(12|34)', 'zzAB34zz').group()
