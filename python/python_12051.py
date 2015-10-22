# find a capital in a string. No loops. Only if statements and string methods python
has_capital = lambda s:s[0].isupper() or has_capital(s[1:]) if s else False
