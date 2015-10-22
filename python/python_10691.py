# How can I further shorten this Python script which copies the contents of one file to another file?
from sys import argv
open(argv[2], 'w').write(open(argv[1]).read())
