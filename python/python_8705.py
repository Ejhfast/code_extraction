# How to filter pound signs in a file using python?
import shlex
filelines = [' '.join(shlex.split(line,True)) for line in file]
