# Regexp for multiple line C macro in Python
text=re.sub('#([\W\w\s\d])*?(\n.*?\\\\)*\n', '', text, re.S | re.M)
