# Python read from command line arguments or stdin
import fileinput
for line in fileinput.input():
  process(line)
