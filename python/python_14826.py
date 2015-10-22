# Remove characters before inserting key value pairs into dictionary
cdata = csv.reader(f, delimiter = ';', quoting = csv.QUOTE_NONNUMERIC)
print dict(cdata)
