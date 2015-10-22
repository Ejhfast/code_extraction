# Opening an excel file manually allows formulas to run, opening an excel file with VBScript or PowerShell or Python's win32com doesn't
excel.AddIns.Add("C:\Program Files (x86)\PIPC\Excel\PITrendXL.xla").Installed = True
excel.AddIns.Add("C:\Program Files (x86)\PIPC\Excel\pipc32.xll").Installed = True
