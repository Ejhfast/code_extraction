# in python how do I figure out the current path of the os.walk()?
for root, subdirs, files in os.walk(this_path):
  for my_file in files:
    shutil.move(os.path.join(root, my_file), os.path.join(this_path, filename))
