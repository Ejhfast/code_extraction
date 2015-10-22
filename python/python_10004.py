# using walk function in python
for root, dirs, files in os.walk(path, '*.txt'):
    out = open(os.path.join(root, '..', '..'), 'a')
    out.write(...)
