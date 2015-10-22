# How to know which file to open (and open it) in Python based on its name matching a pattern?
from glob import glob
file = open(glob('report *')[0])
