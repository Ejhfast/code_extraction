# Read A Multidimesion String Array From File
with open('Path/to/file', 'r') as content_file:
    content = content_file.read()
    data = json.loads(content)
