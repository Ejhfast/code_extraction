# Python text processing with regular expression
str = re.sub(r'(options) (\S+)', r'\2\n    \1', re.sub(r'([ \t =,])/', replace_text, text))
