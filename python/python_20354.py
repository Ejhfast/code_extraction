# Sorting a file based on Ist column and simultaneously modifing the 2nd column also in the file
with open('filename.txt', 'w') as fout:
     for line in sorted(open('filename.txt', 'r').readlines(), key=lambda x:float(x.split()[0])):
         fout.write(line)
