# how to tell cgi to stop waiting
import sys
sys.stdout.close()
sys.stderr.close()
