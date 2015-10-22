# Making io.BufferedReader from sys.stdin in Python2
reader = io.open(sys.stdin.fileno())
