# How to distinguish between local filesystem path and file system path over SSH?
pattern = '(\.?/|/)|(^:?[^:]*$)'
re.match(pattern, ":home/test") # match, is a local path
re.match(pattern, "user@host:blah") # no match
