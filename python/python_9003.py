# split a comma, space, or semicolon separated string using regex
str = 'a,,b,c,'
re.findall(r'[^,;\s]+', str)
