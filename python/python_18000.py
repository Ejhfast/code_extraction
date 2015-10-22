# python write to file from a dictionary in batch
for row in dictrows:
    out_f.write("%s%s" %(delimiter.join([row[name] for name in fieldnames]),
                lineterminator))
