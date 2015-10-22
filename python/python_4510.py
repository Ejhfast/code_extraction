# Python. Print mac address out of 6 byte string
import struct
"%x:%x:%x:%x:%x:%x" % struct.unpack("BBBBBB",your_variable_with_mac)
