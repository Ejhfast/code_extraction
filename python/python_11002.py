# Reverse DNS lookup in Python
from dns import resolver,reversename
addr=reversename.from_address("2001:4860:4860::8888")
str(resolver.query(addr,"PTR")[0])
