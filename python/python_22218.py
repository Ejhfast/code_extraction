# In Jython, how can I create unicode string from UTF-8 byte sequence?
a = [0xE3, 0x81, 0x82]
print "".join([chr(c) for c in a]).decode('UTF-8')
