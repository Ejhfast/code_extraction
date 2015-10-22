# Replace pairs of characters at start of string with a single character
re.sub(r'^(-+)\1', r'\1', "------foo--bar")
