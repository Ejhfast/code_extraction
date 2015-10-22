# How does one get all files in a directory with a specific pattern in their names in Python
name = 'Project_Name'
glob.glob(os.path.join(directory, '{}_*.txt'.format(name)))
