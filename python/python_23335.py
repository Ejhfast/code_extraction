# How do I get the value of OpenSSL._util.lib.X509_verify_cert_error_string as a python string
from OpenSSL._util import ffi
ffi.string(lib.X509_verify_cert_error_string(errornum))
