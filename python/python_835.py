# What's the regex for removing dots in acronyms but not in domain names?
re.sub('\.(?!(\S[^. ])|\d)', '', s)
