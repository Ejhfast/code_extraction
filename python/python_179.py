# How to check that a path has a sticky bit in python?
import os
def is_sticky(path):
    return os.stat(path).st_mode &amp; 01000 == 01000
