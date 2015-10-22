# Find a string with newline or whitespace to fix broken xml input
import re
search = re.search(r'&lt;/answ\s', i).start()
