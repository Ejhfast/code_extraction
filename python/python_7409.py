# How to sort environment variables in python
for name, value in sorted(os.environ.items()):
    print("   " + name + "=" + value)
