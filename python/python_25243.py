# Python regex, conditional searching
print re.findall('([A-Z]+[^.].*?[a-z.][.?!] )(?=[^a-z])',text)
