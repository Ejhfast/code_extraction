# python winapi check if sheet exists
'name' in [excel_file.Sheets(i).Name for i in range(1,excel_file.Sheets.Count+1)]
