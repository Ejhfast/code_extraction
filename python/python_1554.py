# Remove lines from textfile with python
lines = open('textfile.txt').readlines()
open('newfile.txt', 'w').writelines(lines[3:-1])
