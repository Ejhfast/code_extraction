# Encrypting strings in python with no knowledge of cryptography
from simplecrypt import encrypt, decrypt
ciphertext = encrypt('password', plaintext)
plaintext = decrypt('password', ciphertext)
