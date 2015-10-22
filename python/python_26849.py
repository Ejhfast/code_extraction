# Regex to extract names based on patterns in values from a list of name value pairs
re.findall(r"\('([^']+)', 'NN[^']?'\)", x)
