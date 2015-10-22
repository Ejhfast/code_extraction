# How to get text file from a relative path?
import os
open(os.path.join(os.path.dirname(__file__), 'Directory', 'input.txt'))
