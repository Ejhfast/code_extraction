# Opening and reading UTF-16 files in Python
with open(filename, "rb") as data:
    header = data.read(24)
    text = data.read().decode('utf-16-le')
