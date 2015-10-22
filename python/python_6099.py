# Can I make uuid's more random?
import hashlib
actually_random = hashlib.sha1(uuid).digest()
