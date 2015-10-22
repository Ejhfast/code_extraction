# Convert hex-string to string using binascii
s=str(616263)
print "".join([chr(int(s[x:x+2], 16)) for x in range(0,len(s),2)])
