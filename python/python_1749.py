# How to read from stdin or from a file if no data is piped in Python?
import fileinput
for line in fileinput.input(remaining_args):
    process(line)
