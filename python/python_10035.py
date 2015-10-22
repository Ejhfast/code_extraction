# How do I check if a string only contains alphanumeric characters and dashes?
import re
valid = re.match('^[\w-]+$', str) is not None
