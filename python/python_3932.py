# Python list.remove() seems to malfunction
with open(filedir) as f:
    lines = [line.rstrip("\r\n") for line in f if line.startswith("@")]
