# Convert simple php code to python
import hashlib
secret, path, expire = 'segredo', '/p/files/top_secret.pdf', 1096891200
md5 = hashlib.md5(secret + path + str(expire)).digest().encode('base64').strip('\n=')
