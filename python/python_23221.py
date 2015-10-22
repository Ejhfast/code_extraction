# regex for repeating words in a string in Python
re.sub(r'(?&lt;!\S)((\S+)(?:\s+\2))(?:\s+\2)+(?!\S)', r'\1', s)
