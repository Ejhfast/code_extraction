# Yowsup Authentication don't work
import base 64
 password= 'randomletters+somenumbers=' #Get this by registering
 password = base64.b64decode(bytes(rawPass.encode('utf-8')))
