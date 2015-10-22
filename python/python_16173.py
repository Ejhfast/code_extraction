# Remove a network printer with Python's wmi module?
for printer in c.win32_printer():
    if printer.DEVICEID == "\\\\server\\printer":
    printer.delete_()
