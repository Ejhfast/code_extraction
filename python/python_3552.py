# Cleaning and stripping of strings/HTML - Python
stripped_iter = (x.strip() for x in l.split(','))
non_empty_iter = (x for x in stripped_iter if x)
