# Reference list item as key in sorted for loop
sorted(os.listdir('.'), key=lambda f: int(f.split('.')[0][1:]))
