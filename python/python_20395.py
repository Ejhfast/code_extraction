# Trying to write a string to a tempfile
filename = tfile.name
fullfilename = filename + ".gz"
gzip.open(fullfilename,"wb")
