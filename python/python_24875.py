# Create a function which reads all lines of code from text file and put each line into tuples. -Python 3
with open("studs.txt") as f:
    for line in f:
        print(line.split())
