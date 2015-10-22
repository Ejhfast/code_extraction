# pythonic manner of merging last three columns into a single pipe seperated column
line = line[:-3] + ['|'.join(line[-3:])]
