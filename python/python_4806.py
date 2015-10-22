# Run Windows CMD commands via Python
cmdprocess.stdin.write(("mklink " + linkname + " " + fullname + "\r\n").encode("utf-8"))
