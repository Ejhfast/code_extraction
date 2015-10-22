# Using Pandas to pd.read_excel() for multiple worksheets of the same workbook
xls = pd.ExcelFile('path_to_file.xls')
df1 = xls.parse('Sheet1')
df2 = xls.parse('Sheet2')
