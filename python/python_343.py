# Rename files, Python/Jython
import glob, os
for filename in glob.glob(os.path.join(yourPath, "*&amp;*")):
   os.rename(filename, filename.replace('&amp;','+'))
