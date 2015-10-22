# How to retain only letter, digit, space using at most re module?
return re.sub(r'[^a-zA-Z0-9\s]+','',text).lower().strip()
