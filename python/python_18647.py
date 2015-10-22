# Sort tuple by last name
with open('trash.txt', 'r') as fin:
    for line in sorted(fin, key=lambda x:x.split(',')[1]):
        print line
