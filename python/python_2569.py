# Reading Japanese filenames in windows, using Python and glob not working
path = u'G:\path'
for infile in glob.glob( os.path.join(path, u'*') ):
    print( u"current file is: ", infile)
