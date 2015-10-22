# Python split() without removing the delimiter
d = "&gt;"
for line in all_lines:
    s =  [e+d for e in line.split(d) if e != ""]
