# How to load an RSA key from a PEM file and use it in python-crypto
pk = open( 'public_key.pem', 'rb' ).read()
rsa = M2Crypto.RSA.load_pub_key(pk)
