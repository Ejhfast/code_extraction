# Writing unicode data in csv
ff = open('a.csv', 'w')
ff.write(codecs.BOM_UTF8)
