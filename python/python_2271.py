# How to replace only part of the match with python re.sub
re.sub(r'(?:_a)?\.([^.]*)$', r'_suff.\1', "long.file.name.jpg")
