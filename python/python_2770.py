# How to efficiently output dictionary as csv file using Python's csv module? Out of memory error
for row in dictrows:
    out_f.write("%s%s" %(delimiter.join([row[name] for name in fieldnames]),
                         lineterminator))
