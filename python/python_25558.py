# regular expression to extract numerical values
print '\t'.join([line.strip().split()[-1] for line in infile])
