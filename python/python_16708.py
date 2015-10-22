# using regular expression substitution command to insert leading zeros in front of numbers less than 10 in a string of filenames
re.sub('[a-zA-Z]\d,', lambda x: x.group(0)[0] + '0' + x.group(0)[1:], s)
