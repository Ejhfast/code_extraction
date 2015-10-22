# Find a replace string in xml file with python
for line in fileh:
    line = line.replace("enabled", "disabled")
    ouf.write(line)
