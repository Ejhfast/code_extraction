# Python win32com method for word-wrap in Excel?
for i in range(0,active_sheets):
    ws = wb.Worksheets(i+1)
    ws.Columns.WrapText = True
