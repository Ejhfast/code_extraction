# change first line of a file in python
from_file.readline() # and discard
to_file.write(replacement_line)
shutil.copyfileobj(from_file, to_file)
