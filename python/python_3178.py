# Signing a string with RSA private key on Google App Engine Python SDK
from tlslite.utils import keyfactory
private_key = keyfactory.parsePrivateKey(rsa_key)
signed = private_key.hashAndSign(data)
