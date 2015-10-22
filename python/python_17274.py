# Python csv.writer control precision
wr = csv.writer(f, quoting=csv.QUOTE_NONE)
for i in output:
    wr.writerow(['{:3.4e}'.format(x) for x in i])
