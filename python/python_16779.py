# Python: Find newest file with .MP3 extension in directory
import os
import glob
newest = max(glob.iglob('*.[Mm][Pp]3'), key=os.path.getctime)
