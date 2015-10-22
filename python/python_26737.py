# if item in list match item in list from child element in dictionary
if os.path.isdir(os.path.join(directory, subdir)) and [i for i in testnames.values() if subdir.lower() in i['names']]:
