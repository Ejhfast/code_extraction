# python xlrd convert xlsx to csv
for rownum in xrange(sheet.nrows):
      wr.writerow([unicode(val).encode('utf8') for val in sheet.row_values(rownum)])
