# Python reverse replace
decipher = dict(zip(numbs1,chars))
stringc = ''.join(decipher[stringb[i:i+2]] for i in range(0, len(stringb), 2));
print "Decoded: ", stringc
