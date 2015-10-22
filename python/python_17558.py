# Dynamically Create Variables in For Loop, Python
for row in ws.iter_rows():
    # row is now a tuple
    first_value = row[0]
