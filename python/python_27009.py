# Remove non Unicode characters from xml database with Python
for line in somefile:
    uline = line.decode('ascii', errors='ignore')
