# Python list of strings and list of regexes, clean way to find strings which don't match anything?
[key for key in keys if not any(re.match(pattern, key) for pattern in patterns)]
