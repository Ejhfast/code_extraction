# Set files to ownership of current directory in Python
import os, stat
info = os.stat(dirpath)
uid, gid = info[stat.ST_UID], info[stat.ST_GID]
