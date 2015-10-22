# Iterating through individual files in os.walk in Python in an idiomatic fashion
result = [os.path.join(root, file) for root, dir, files in os.walk(mydir) for file in files]
