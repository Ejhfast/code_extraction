# Remove all <word> tags
lines = file_variable.read()
print re.subn('&lt;.*?&gt;', ' ', line)
