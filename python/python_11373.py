# How to obtain sheet names from XLS files without loading the whole file in Python?
import xlrd
xls = xlrd.open_workbook(r'&lt;path_to_your_excel_file&gt;', on_demand=True)
print xls.sheet_names() # &lt;- remeber: xlrd sheet_names is a function, not a property
