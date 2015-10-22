# How do I tell a Python script (cygwin) to work in current (or relative) directories?
import os
print os.path.normpath(os.path.join(os.getcwd(), '../AnotherBook/Chap2.txt'))
