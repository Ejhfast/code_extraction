# Python: How can I find all files with a particular extension?
results += [each for each in os.listdir(folder) if each.endswith('.c')]
