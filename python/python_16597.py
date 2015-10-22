# Python loops through CSV, but writes header row twice
with open('file.csv', 'r') as src, open('file2.csv', 'w') as dst:
    dst.write(next(src).replace(" ", ""))     # delete whitespaces from header
    dst.writelines(line for line in src)
