# trying to convert hex to binary and xor the result
return ''.join((chr(ord(a) ^ ord(b))) for a,b in zip(s1.decode('hex'),
  s2.decode('hex'))).encode('hex')
