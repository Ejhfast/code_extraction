# converting string to int python
import re
src = ['(111,11,12)', '(12,34,56)']
[tuple([int(n) for n in re.findall(r"(\d+),(\d+),(\d+)", s)[0]]) for s in src]
