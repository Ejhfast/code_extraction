# how to get a list of all the folders in current directory
[f for f in os.listdir('.') if os.path.isdir(f)]
