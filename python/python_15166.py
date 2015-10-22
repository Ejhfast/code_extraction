# Python list comprehension, can it be used for reading multiple files?
[map(str.rstrip, f.readlines()) for f in files]
