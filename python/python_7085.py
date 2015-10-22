# Pycurl keeps printing in terminal
p.setopt(pycurl.WRITEFUNCTION, lambda x: None)
