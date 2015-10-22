# What would be a good way to deal with backslash escaped characters?
re.split(r'(?&lt;!\\),', 'part1,part2,pa\\,rt3,part4')
