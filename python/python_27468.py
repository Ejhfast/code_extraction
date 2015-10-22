# how to remove tokens that contains number followed by character using regular expression in python?
re.sub(r"[0-9]+[a-z]+","",str)
