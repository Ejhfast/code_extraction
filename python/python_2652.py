# Trying to match '#' in a text
result = re.findall("(?:^|\s)(#[a-zA-Z]+)", text, re.MULTILINE)
