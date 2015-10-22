# Counting the occurence of a specific string in a csv file
with open('Path/to/file', 'r') as content_file:
    content = content_file.read()
    print(content.count("Methadone"))
