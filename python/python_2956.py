# Writing only part of a line to a file
for line in infile:
    line = line.strip().split(',')
    outfile.write(','.join(line[:3]) + '\n')
