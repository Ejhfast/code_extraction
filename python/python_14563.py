# Python: Regex a dictionary using user input wildcards
with open('testfilefolder/wssnt10.txt') as f:
 file_contents = f.read().lower().split(' ') # split line on spaces to make a list
 filtered = fnmatch.filter(file_contents, 'th*')
