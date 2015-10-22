# Is there a way to find out the name of the file stdout is redirected to in Python
import os
my_output_file = os.readlink('/proc/%d/fd/1' % os.getpid())
