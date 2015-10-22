# Python 3.3.2 - Sorting a List, While Disregarding Vowels
import re
new_list = sorted(l, key=lambda s: re.sub('[aioue]', '', s))
