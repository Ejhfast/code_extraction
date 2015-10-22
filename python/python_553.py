# How to write binary data in stdout in python 3?
import sys
sys.stdout.buffer.write(b"some binary data")
