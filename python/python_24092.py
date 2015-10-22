# Convert an input file to ascii python
file_content = open(file, 'r').read()
file_content = ''.join(str(ord(c)) for c in file_content))
open('Output.txt','w').write(file_content)
