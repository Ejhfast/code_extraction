# File Sorting in Python
f2.writelines(sorted(f1, key=lambda line:int(line.split()[0])))
