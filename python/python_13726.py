# Pylint not working as expected
for filename in f:
    if filename.endswith(".py"):
        os.system("pylint %s &gt;&gt; output.txt" % os.path.join(r, filename))
