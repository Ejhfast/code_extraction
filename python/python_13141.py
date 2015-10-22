# How to authenticate hashed(sha1) password in Python?
import hashlib
s = "plain"
h = hashlib.sha1(s).hexdigest()
