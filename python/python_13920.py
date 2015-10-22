# Python subprocess: Why does stdin=PIPE change the output of some commands?
import sys
print sys.stdin.isattty()   # True if it's a terminal, False if it's redirected
