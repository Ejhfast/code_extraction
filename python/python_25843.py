# Representing a number using two bytes
from struct import pack, unpack
unpack('BB', pack('H',300))
# gives (44, 1), the two bytes you were asking for
