# It's probably simpler in awk, but how can I say this in Python?
import re
# read the book into a variable 'text'
matches = re.findall(r'\w+ is for \w+ \w+ing his \w+', text)
