# Iterate thru Excel column A , write to column B using Python win32
col = ws.Range("A1:A100")
for cell in col:
    cell.Offset(1,2).Value = "W0000%s" % cell.Value
