# Append binary file to another binary file
with open("binary_file_1", "ab") as myfile, open("binary_file_2", "rb") as file2:
    myfile.write(file2.read())
