# How to list only down-most directories in Python?
for dirpath, dirnames, filenames in os.walk(mydir):
    if not dirnames:
        print dirpath, "has 0 subdirectories and", len(filenames), "files"
