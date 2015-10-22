# Pythonic way to remove directories from a file listing
[x for x in os.listdir(...) if not os.path.isdir(os.path.join(..., x))]
