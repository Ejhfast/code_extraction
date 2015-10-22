# Parsing from Shakespeare text in Python
re.split(r"(?:^|(?:[^\S\n]*\n){2}(?m)^)[ \t]+\d+[ \t]+[\r\n]+", text)
