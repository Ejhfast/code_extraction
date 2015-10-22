# Can I use a List Comprehension to get Line Indexes from a file?
[index for index,line in enumerate(open('myfile.txt')) if 'mystring' in line]
