# How to pass a function to another function in python
def run(func):
    for line in sys.stdin:
        print func(line)
