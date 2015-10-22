# Is there more simple way to change list elements
for i, line in enumerate(report['ipconfig']):
    report['ipconfig'][i] = line.decode('cp866')
