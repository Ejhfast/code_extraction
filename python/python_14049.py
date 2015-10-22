# dbf to xls - first non header row not writing
for row in range(len(dbf)):
    for col in range(len(dbf.fieldNames)):
        sheet1.row(row+1).write(col, dbf[row][col])
