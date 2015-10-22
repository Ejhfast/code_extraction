# get also element that don't match fnmatch
goodfiles = fnmatch.filter(files, pattern)
badfiles = set(files).difference(goodfiles)
