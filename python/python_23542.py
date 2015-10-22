# Slice a message from python string
re.search(r"message\s+=\s+'([^']*)'",text_string,re.M).group(1)
