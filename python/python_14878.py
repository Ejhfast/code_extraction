# Windows/Py3 stdout with only LR, not CRLF
import sys,os
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', newline='')
print("Whatever")
