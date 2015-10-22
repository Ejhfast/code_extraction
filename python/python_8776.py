# Python Reg expression to delete all text inside quotation marks
text = 'According to James, "we do not know" the source of the problem, "we are clueless".'
re.sub('".+?"', '', text)
