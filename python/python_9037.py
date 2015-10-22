# Can anyone show me how to do this without using loops?
files = ['title1.pdf', 'title2.pdf', 'title3.pdf']
files += [ "%.2d.pdf" % j for j in range(1,100)]
pages = [[folder+file for file in files] for folder in foldernames]
