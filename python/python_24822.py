# Sorting a file in ascending order
with open('myInput01.txt') as fin, open('myOutput01.txt', 'w') as fout:
    fout.writelines(sorted(fin))
