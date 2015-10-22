# Sort list of filenames by number
sorted(glob.glob('*.dat'), key=lambda x: int(x.split('.')[0][4:]))
