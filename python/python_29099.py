# Reading DAT File
with open("contacts.dat") as infile:
    file_contents = infile.readlines()
print(file_contents)
