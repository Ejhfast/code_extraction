# Error when using Python to create hyperlink within a worksheet in Excel
def CreateLink():
    excel.Worksheets(1).Cells(1,1).Value = '=HYPERLINK(A21,"Cell A21")'
