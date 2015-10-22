# Regular Expression to remove html tags from a string in Python
pattern = re.compile(u'&lt;\/?\w+\s*[^&gt;]*?\/?&gt;', re.DOTALL | re.MULTILINE | re.IGNORECASE | re.UNICODE)
text = pattern.sub(u" ", text)
