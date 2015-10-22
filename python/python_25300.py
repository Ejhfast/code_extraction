# Access command line arguments as bytes in python3
#!/usr/bin/python3
import sys
arg1_bytes = sys.argv[1].encode(sys.getfilesystemencoding(), 'surrogateescape')
