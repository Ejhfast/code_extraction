# Paramiko: Creating a PKey from a public key string
# For a public key "ssh-rsa AAblablabla...":
key = paramiko.RSAKey(data=base64.b64decode('AAblablabla...'))
key.verify_ssh_sig(..., ...)
