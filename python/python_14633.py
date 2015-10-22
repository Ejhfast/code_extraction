# How to extract a text string using bash (or python on mac)
grep -E "[0-9]+ (month|year|day|week)s? ago" a.txt| grep -Eo "^[a-zA-Z0-9]+"
