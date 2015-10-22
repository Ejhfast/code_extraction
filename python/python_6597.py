# IMAP Fetch Encoding
from email.header import decode_header
value, charset = decode_header(string_to_be_decoded)
