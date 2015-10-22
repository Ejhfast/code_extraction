# Check key algorithm with Python
from OpenSSL import crypto
cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_string)
cert.get_signature_algorithm()
