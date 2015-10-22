# Python - Importing Excel dates converts to number
wb = xlrd.open_workbook("somewb.xls")
my_date_tuple = xlrd.xldate_as_tuple(xls_timestamp_number,wb.datemode)
