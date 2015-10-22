# Get time zone information of the system in Python?
from time import gmtime, strftime
print strftime("%z", gmtime())
