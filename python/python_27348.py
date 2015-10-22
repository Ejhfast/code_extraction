# ASCII files get erased after opening in Python
with open('E:\ASCII\data.txt', 'r') as f:
    for line in f.read().splitlines():
        print repr(line)
