# End-line characters from lines read from text file, using Python
for line in open('myfile.txt'):  # opened in text-mode; all EOLs are converted to '\n'
    line = line.rstrip('\n')
    process(line)
