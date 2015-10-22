# Replacing leading and trailing hyphens with spaces?
re.sub(r'^-+|-+$', lambda m: ' '*len(m.group()), '---ab---c-def--')
