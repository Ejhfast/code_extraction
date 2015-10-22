# searching multiple items with Python re
hrs, min, sec, msec = (int(group) for group in re.search('(\d+):(\d+):(\d+).(\d+)', current_line).groups())
