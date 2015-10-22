# Delete duplicate rows in textfile - except it contains a "{" or "}"
if ('{' in line or '}' in line) and line not in lines_seen: # not a duplicate
