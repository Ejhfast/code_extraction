# How to insert data from a SQL SELECT into a spreadsheet
for number, row in enumerate(cursor.fetchall()):
    for column, cell in enumerate(row):
        sheet.write(number, column, cell)
