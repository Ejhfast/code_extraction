# Python: Check if string matches pattern
import re
pattern = re.compile("^([A-Z][0-9]+)*$")
pattern.match(string)
