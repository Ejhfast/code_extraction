# moving files inside a directory
for file in os.listdir('path/to/parent'):
    move('path/to/parent'+os.path.sep+file, '/path/to/new_parent')
