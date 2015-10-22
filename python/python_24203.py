# How to sha256 hash a variable in Python
var = 'password'
hashedWord = sha256(var.encode('ascii')).hexdigest()
