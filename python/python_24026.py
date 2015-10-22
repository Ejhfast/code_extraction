# How to write two sheets in a single workbook at the same time using openpyxl
ws1 = wb.active
ws2 = wb.create_sheet()
