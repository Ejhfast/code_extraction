# With Python can you use regex to grep through a file without pulling it all into memory?
with open('./data.txt') as data:
    for line in data:
        print exp.search(data)
