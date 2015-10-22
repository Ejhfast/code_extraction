# How to generate random IPv6 address using Python(or in Scapy)?
import random
M = 16**4
"2001:cafe:" + ":".join(("%x" % random.randint(0, M) for i in range(6)))
