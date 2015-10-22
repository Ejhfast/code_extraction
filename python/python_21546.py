# How to put in the thousands separator in xlsx using xlsxwriter module?
num_fmt = workbook.add_format({'num_format': '#,###'})
...
sheet.write_number(0, 0, 1000, num_fmt)
