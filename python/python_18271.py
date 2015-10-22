# Extract a zip file in python [zip file contains .img file in it, and zipfile gets stuck]
z = zipfile.ZipFile(file_name)
z.extractall()
