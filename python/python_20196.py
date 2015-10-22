# How to print part of output from a subprocess
for line in p.stdout:
    if "Number of" in line:
        print line
