# Append columns to python cursor before writing to CSV?
writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
for row in cursor:
    writer.writerow(list(row) + ['', '', '', ''])
