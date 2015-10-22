# How to copy a table from excel to word using pythonCOM
sheet.Range("A1:D20").Copy()
doc.Content.PasteExcelTable(False,False,False)
