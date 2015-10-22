# Renaming File Names Using Python
e = int(filename[-6:-4])
new_filename = '%s%02d-E%02d%s' % (filename[:-6], e*2-1, e*2, filename[-4:])
