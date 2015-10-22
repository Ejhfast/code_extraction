# Python corrupts pdf after download from file
pdf = open(filename, 'rb')
response = HttpResponse(pdf.read())
