# Returning all characters before the first underscore
re.sub("[^A-Z\d]", "", re.search("^[^_]*", str).group(0).upper())
