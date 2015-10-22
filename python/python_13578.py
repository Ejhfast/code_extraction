# Issue with creating "xlsx" in Python by copying data from csv
for rowx,row in enumerate(reader):
    for colx, value in enumerate(row):
        ws.cell(row=rowx,column=colx).value = unicode(value, "mbcs")
