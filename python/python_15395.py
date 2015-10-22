# Removing strings containing ASCII
import re
re.sub(r'[^\x00-\x7f]+', " ", inputString)
