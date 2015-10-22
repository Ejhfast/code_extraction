# Python Regular Expressions: Capture lookahead value (capturing text without consuming it)
re.findall("([%]+)([^%]+)(?=([%]+))".replace("%", "".join(VOWELS)), word)
