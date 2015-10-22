# urllib does not handle # character properly
from six.moves.urllib import parse
o=parse.urlparse('http://me:me1234%23@localhost:8080/')
print o
