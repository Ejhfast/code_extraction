# open the file in universal-newline mode using csv module django
mypath = customerbulk.objects.get(pk=1).fileup.path
o = open(mypath,'rU')
mydata = csv.reader(o)
