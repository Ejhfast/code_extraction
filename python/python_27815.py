# How to read from STDIN in python from a piped grep output
import sys
log = "".join([i for i in sys.stdin])
print log
