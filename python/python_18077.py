# Stripping headers and footers
private_key = private_key.replace('-----BEGIN RSA PRIVATE KEY-----', '')
private_key = private_key.replace('-----END RSA PRIVATE KEY-----', '')
