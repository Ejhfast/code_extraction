# Why does this regular expression not capture requested groups?
r = re.findall(r'^ \s+ (\w+) \s+ ((?:0x [\da-f]+ \s+)*)', oo, re.VERBOSE)
numbers = r[0][1].split()
