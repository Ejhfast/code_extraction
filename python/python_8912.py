# Raw string in Python regular expression using Windows folder path
import re
print re.sub(r'^[a-zA-Z]:\\.+(\\Data.+)', r'D:\\folder\1', r'C:\Some\Path\Data\File.txt')
