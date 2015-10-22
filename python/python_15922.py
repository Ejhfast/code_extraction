# Re.sub regex delete nested brackets python
re.sub(r'\(\d*\D+\d*\)\s+','',re.sub(r'\{.+?\#(\d+)\.\d+\)}',r'(\1)',s))
