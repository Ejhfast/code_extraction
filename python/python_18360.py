# Sorting a dictionary which is exported to excel?
for key in sorted(finaldict.keys()):
    writer.writerow([key] + finaldict[key])
