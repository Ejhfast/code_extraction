# How to make only some strings of nested lists into integers?
nested = [line.strip().split(',') for line in in_file][1:]
nested = [line[:1] + [int(x) for x in line[1:]] for line in nested]
