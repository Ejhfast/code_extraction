# Reading a file from Google Cloud Storage with XLRD (python)
archivo=cloudstorage.open('/bucket/workbook.xlsx')
wb = xlrd.open_workbook(file_contents=archivo.read())
