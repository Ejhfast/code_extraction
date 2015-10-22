# Encoding utf-8 to base64 with accents
base64.b64encode("Hi, %s! Your code is %s" % (data[0].decode('utf8').encode('latin1'), data[0]))
