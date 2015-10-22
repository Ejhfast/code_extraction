# read a very big single line txt file and split it
import os
with open('infile.txt') as f_in, open('outfile.txt', 'w') as f_out:
  f_out.write(f_in.read().replace('ROW_DEL ', os.linesep))
