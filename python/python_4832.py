# How to remove underscore('_') along with preceeding digits in first columns only
re.sub(r"(\.\d+)_\d+", r"\1", line)
