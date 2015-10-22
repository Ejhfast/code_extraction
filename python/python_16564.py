# Generating binary objects of size N, with N being specified by the user
with open("filename", "wb") as f:
    f.seek(10239)    # seek to 10k - 1
    f.write("\0")    # write a single byte
