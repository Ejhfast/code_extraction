# DES.MODE_OFB doesn't recover the plaintext
decCipher = DES.new(key, DES.MODE_OFB, msg[:DES.block_size])
msgback = decCipher.decrypt(msg[DES.block_size:])
