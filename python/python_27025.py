# Checking permission of a file using python
if os.access("/data/lims/LI", os.X_OK):
     print "pass"
