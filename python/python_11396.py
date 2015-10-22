# python change string between certain two words
import re
re.sub('(StartNum)(.*)(/StartNum)', r"\1boop\3", 'StartNumbworp/StartNum')
