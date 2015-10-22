# python - read file lines and place it in array
with open('screennames.txt') as namefile:
    screennames = ','.join(map(str.rstrip, namefile.readlines()))
