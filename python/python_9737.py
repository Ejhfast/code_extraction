# Getting Type error while opening an uploaded CSV File
paramFile = request.FILES['uploadFile'].read()
portfolio = csv.DictReader(paramFile)
