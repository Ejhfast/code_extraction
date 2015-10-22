# removing extra blank spaces in python
import re
removedSpaces = re.sub(r'\n{3,}', "\n\n", lineWithSpaces)
