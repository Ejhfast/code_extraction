# How can I find a method name not within a comment?
re.search("^(?!\/\/)\s*void aMethod",line)
