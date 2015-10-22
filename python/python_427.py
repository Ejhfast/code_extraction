# Python: Read a file (from an external server)
import urllib
content = urllib.urlopen('http://www.google.com/').read()
