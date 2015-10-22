# How to convert strings numbers to integers in a list?
changed_list = [int(f) if f.isdigit() else f for f in original_list]
