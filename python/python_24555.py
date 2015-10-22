# For row in read limitation python
for row in itertools.islice(read, stop = rownum):
    out_writer.writerow(row)
