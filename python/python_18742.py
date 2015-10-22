# Python regex replace, with lambda function, overwriting non-capturing groups
_l = re.sub(r'(?:\=|\=\&gt;|\()\s*(true|false|null)\s*(?:\)|\;|\,)', lambda pattern: pattern.group(0).upper(), _l)
