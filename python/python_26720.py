# reading file to check for same number of delimiters
with open(file_name) as your_file:
    start = your_file.readline().count(',') # initial count
    print all(i.count(',') == start for i in your_file)
