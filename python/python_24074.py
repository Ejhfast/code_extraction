# Deletion of Read only files on a windows machine running a python script
import os, stat
os.chmod(path, stat.S_IWRITE)
os.unlink(path)
