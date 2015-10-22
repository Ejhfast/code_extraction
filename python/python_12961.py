# Cheap mapping of string to small fixed-length string
cheap_hash = lambda input: hashlib.md5(input).hexdigest()[:6]
