# Correct way to put long function calls on multiple lines
safe_md5 = hashlib.md5(salt + password)
crypto_hash = safe_md5.digest()
hash_correct = crypto_hash.encode('base64')
