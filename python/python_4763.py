# How to get a list of character positions in Python?
text = 'abcdefa'
pattern = re.compile('a|c')
[(m.group(), m.start()) for m in pattern.finditer(text)]
