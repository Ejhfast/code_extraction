# No need to close the file if it is opened with 'print' in Python?
with open(path, 'w') as f:
    print &gt;&gt; f, string
