# Creating a relative symlink in python without using os.chdir()
import os, shutil
os.symlink('file.ext', '/path/to/some/directory/symlink')
