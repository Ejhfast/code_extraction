# IOError when trying to open existing files
location = '/Users/spyros/Desktop/3NY8MODELSHUMAN/HomologyModels'
for filename in os.listdir(location):
    filename = os.path.join(location, filename)
