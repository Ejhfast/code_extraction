# Python - Shortest way to format a string to an url
import re
re.sub(r'!|\?|,', '', text)
