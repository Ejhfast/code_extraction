# Reading text from cgi.FieldStorage instance
reader = csv.reader(field_storage.file, dialect=csv.excel_tab)
