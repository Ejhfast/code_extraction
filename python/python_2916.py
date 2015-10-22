# How do I efficiently fill a file with null data from python?
with open(filename, "wb") as f:
    f.seek(999999)
    f.write("\0")
