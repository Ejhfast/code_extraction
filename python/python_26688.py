# Python Search the specific word sequence from the pos sequence and highlight it
import re
re.sub(r'((?:He|well.*?made|Italian.*?American).*?)(\s)', r'[\1]\2', string)
