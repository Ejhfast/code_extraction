# Reordering python list based on an algorithm or pattern
brokenlist = sorted(range(1, 44), key=str)
brokenmap = [x[0] for x in sorted(enumerate(sorted(range(1, 44), key=str)), key=lambda x: x[1])]
fixedlist = [brokenlist[x] for x in brokenmap]
