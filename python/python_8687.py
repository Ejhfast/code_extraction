# How can I check if a list of patterns is not there in my list of filenames?
files = [f for f in files if not f.endswith(('.pdf', '.mpeg'))]
