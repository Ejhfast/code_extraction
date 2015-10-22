# Function to select a range of data files with different number extensions
list = []
    for filelist in [glob.glob(pattern) for pattern in ['*%i*' % x for x in range(a,b+1)] if glob.glob(pattern)]:
        list += filelist
