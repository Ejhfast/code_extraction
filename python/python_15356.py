# Regex. How to remove multiple occurence of 'u' if it's befoure some symbol
import re
print re.sub(r"u('\w)", r"\1", p)
