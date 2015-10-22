# What is the Python equivalent of Perl's FindBin?
import os
import sys
bindir = os.path.abspath(os.path.dirname(sys.argv[0]))
